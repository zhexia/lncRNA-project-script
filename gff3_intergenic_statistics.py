# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:49:18 2018

@author: 桑叶
"""

#python3 gff3_intergenic_statistics.py test1_genome.gff >> intergenic_region_avelength.txt

import sys
import gffutils
from collections import defaultdict
import os
                  
path = os.getcwd() 
geneDict = defaultdict(list)
fn = gffutils.example_filename(path+'/'+sys.argv[1])
db = gffutils.create_db(fn, ":memory:", merge_strategy='create_unique', keep_order=True)
for geneline in db.features_of_type('gene'):
    info = str(geneline).split()
    geneDict[str(info[0])].append((int(info[3]),int(info[4])))

num = 0
sumlength = 0
for chromekey,geneloci in geneDict.items():
    for locus in geneloci:
        if locus == geneloci[0]:
            index = locus[1]
        else:
            if locus[0] > index:
                length = locus[0] - index - 1
                sumlength = sumlength + length
                num = num + 1
            index = locus[1]
if sumlength != 0:                 
    avelength = sumlength/num      
    print(' '.join(sys.argv[1].split('_')[0:2])+' genome intergenic region average length is: {}'.format('%.2f'%avelength))
else:
    print('please check the gff file')