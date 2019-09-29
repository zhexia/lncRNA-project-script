#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 10:38:39 2019

@author: zhangxuan

Current version 1.0

Next step:
    1. Bio_type pie plot.
    2. 长度分布四分位数。
"""

import sys
import os
import datetime
import numpy as np
from optparse import OptionParser
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import gffutils

inputFile = sys.argv[1]
usage = '''
    After transcriptome assembly, we need to statistic GFF or GTF 
    files. This can help us to adjust assembly parameters.

    The default output folder is gff2stat.

    The input file can be a GTF or GFF files.

    Alternatively, you can specify the filenames directly with
    :option:`-i`/:option:`--input-file` and
    :option:`-o`/:option:`--output-dir` option.

    Example::

        gff_stat_vistualizition.py -i test.gtf -o output_folder
'''

parser = OptionParser(usage)
parser.add_option('-i', '--input-file', dest='gff', help='read gtf or gff file', metavar="FILE", action = "store", type="string")
parser.add_option("-o","--output-dir", dest="gff2statdir", help="save file to this directory", default="gff2statdir", metavar="FILE", action = "store", type="string")

(options, args)=parser.parse_args()

if not os.path.exists(options.gff):
    parser.print_help()
    sys.exit()

os.system('date')
print("read gff file to memory...")

# 读gtf文件
db = gffutils.create_db(options.gff, ':memory:')

# outputdir
outdir = options.gff2statdir

if not os.path.isdir(outdir):
    os.makedirs(outdir, exist_ok=True)


step1 = '''
# ---------------------
# 1. 统计gff中的特征类型
# ---------------------
'''
print(step1)

print("Feature types = ", list(db.featuretypes()))

step2 = '''
# ---------------------
# 2. 统计各个feature数量
# ---------------------
'''
print(step2)

geneCounts = db.count_features_of_type(featuretype="gene")
mRNACounts = db.count_features_of_type(featuretype="transcript")

print({"gene": geneCounts, "transcript": mRNACounts})

## draw plot

plt.figure()
sns.barplot(['Gene', 'Transcript'], [geneCounts, mRNACounts])
plt.title("Feature number statistic")

plt.savefig(os.path.join(outdir, "Feature_number_barplot.pdf"), format='pdf', bbox_inches='tight')

step3 = '''
# ----------------------------------------------------
# 3. 统计一个基因有几个转录本，一个转录本有多少个exon
# ----------------------------------------------------
'''
print(step3)

## gene
genes2transcriptCountList = []

for gene in db.features_of_type("gene"):
    transcriptCounts = len(list(db.children(gene, featuretype='transcript')))
    genes2transcriptCountList.append(transcriptCounts)

print("genes2transcriptCountList:", stats.describe(genes2transcriptCountList))

## exon
transcripts2exonCountList = []

for transcript in db.features_of_type("transcript"):
    exonCounts = len(list(db.children(transcript, featuretype='exon')))
    transcripts2exonCountList.append(exonCounts)

print("transcripts2exonCountList:", stats.describe(transcripts2exonCountList))

## intron
print("update intron information...", sep=' ')
db.update(db.create_introns())

transcripts2intronCountList = []

for transcript in db.features_of_type("transcript"):
    intronCounts = len(list(db.children(transcript, featuretype='intron')))
    if intronCounts:
        transcripts2intronCountList.append(intronCounts)

print("transcripts2intronCountList:", stats.describe(transcripts2intronCountList))

## plot

plt.figure()
plt.suptitle("Feature's children number distribution")
plt.subplots_adjust(hspace =0.6)

plt.subplot(3, 1, 1)
sns.distplot(genes2transcriptCountList, bins=max(genes2transcriptCountList))
plt.xlabel("Transcript number")
plt.ylabel("Gene")

plt.subplot(3, 1, 2)
sns.distplot(transcripts2exonCountList, bins=max(transcripts2exonCountList))
plt.xlabel("Exon number")
plt.ylabel("Transcript")

plt.subplot(3, 1, 3)
sns.distplot(transcripts2intronCountList, bins=max(transcripts2intronCountList))
plt.xlabel("Intron number")
plt.ylabel("Transcript")

plt.savefig(os.path.join(outdir, "Feature_children_number_distribution_distplot.pdf"), format='pdf', bbox_inches='tight')

step4 = '''
# -------------------------------
# 4. 统计各个feature长度分布
# -------------------------------
'''
print(step4)

# gene
geneLens = []

for gene in db.features_of_type("gene"):
    gLen = gene.end - gene.start + 1
    geneLens.append(gLen)

print("geneLens:", stats.describe(geneLens))

# transcript
transcriptLens = []

for transcript in db.features_of_type("transcript"):
    tLen = transcript.end - transcript.start + 1
    transcriptLens.append(tLen)

print("transcriptLens:", stats.describe(transcriptLens))

# exon
exonLens = []

for exon in db.features_of_type("exon"):
    eLen = exon.end - exon.start + 1
    exonLens.append(eLen)

print("exonLens:", stats.describe(exonLens))

# intron
intronLens = []

for intron in db.features_of_type("intron"):
    iLen = intron.end - intron.start + 1
    intronLens.append(iLen)

print("intronLens:", stats.describe(intronLens))


# 基因间区长度分布

chroms = [i['seqid'] for i in db.execute('SELECT DISTINCT seqid FROM features;')]

def genes_on_chrom(chroms):
    """
    Yield genes on `chrom`, sorted by start position
    """
    for g in db.features_of_type('gene', order_by='start', limit=(chroms, 0, 1e9)):
        g.strand = '.'
        yield g

def intergenic(chroms):
    """
    Yield intergenic features
    """
    for chrom in chroms:
        genes = genes_on_chrom(chrom)
        for intergenic in db.interfeatures(genes):
            yield intergenic

intergenicLens = []            
            
for intergenic in intergenic(chroms):
    iLen = abs(intergenic.end - intergenic.start) + 1
    intergenicLens.append(iLen)

print("intergenicLens:", stats.describe(intergenicLens))

## plot

plt.figure()
plt.suptitle('Feature length distribution')
plt.subplots_adjust(hspace =2)

plt.subplot(5, 2, 1)
sns.distplot(np.log10(geneLens))
plt.xlabel("Gene length (log10)")
plt.ylabel("Gene")
plt.subplot(5, 2, 2)
sns.boxplot(np.log10(geneLens))
plt.xlabel("Gene length (log10)")
plt.ylabel("Gene")

plt.subplot(5, 2, 3)
sns.distplot(np.log10(transcriptLens))
plt.xlabel("Transcript length (log10)")
plt.ylabel("Transcript")
plt.subplot(5, 2, 4)
sns.boxplot(np.log10(transcriptLens))
plt.xlabel("Transcript length (log10)")
plt.ylabel("Transcript")

plt.subplot(5, 2, 5)
sns.distplot(np.log10(exonLens))
plt.xlabel("Exon length (log10)")
plt.ylabel("Exon")
plt.subplot(5, 2, 6)
sns.boxplot(np.log10(exonLens))
plt.xlabel("Exon length (log10)")
plt.ylabel("Exon")

plt.subplot(5, 2, 7)
sns.distplot(np.log10(intronLens))
plt.xlabel("Intron length (log10)")
plt.ylabel("Intron")
plt.subplot(5, 2, 8)
sns.boxplot(np.log10(intronLens))
plt.xlabel("Intron length (log10)")
plt.ylabel("Intron")

plt.subplot(5, 2, 9)
sns.distplot(np.log10(intergenicLens))
plt.xlabel("Intergenic length (log10)")
plt.ylabel("Intergenic")
plt.subplot(5, 2, 10)
sns.boxplot(np.log10(intergenicLens))
plt.xlabel("Intergenic length (log10)")
plt.ylabel("Intergenic")

plt.savefig(os.path.join(outdir, "Feature_length_distribution_distplot.pdf"), format='pdf', bbox_inches='tight')

print()
os.system('date')
print("Finished stat. Three pdfs have been saved.")