# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:44:07 2018

@author: chenw
"""
#参数1：.gff 参数2：.fasta 输出：带有位置信息的fasta
import re
import sys

transcripts = dict()
with open(sys.argv[1], 'r') as gff:
        for line in gff:
            item = line.strip().split('\t')
            if (item[2] == "lnc_RNA") or (item[2] == "lnc_RNA"):
                try:
                    transcript_id = re.findall('Genbank:(\S+?)\;', item[8])[0]
                    chrome = item[0]
                    start = item[3]
                    end = item[4]
                    strand = item[6]
                    if transcript_id in transcripts:
                        transcripts[transcript_id].append(chrome)
                        transcripts[transcript_id].append(strand)
                        transcripts[transcript_id].append(start)
                        transcripts[transcript_id].append(end)
                    else:
                        transcripts[transcript_id] = list()
                        transcripts[transcript_id].append(chrome)
                        transcripts[transcript_id].append(strand)
                        transcripts[transcript_id].append(start)
                        transcripts[transcript_id].append(end)
                except:
                    pass
file_out = open(sys.argv[3], 'w')
with open(sys.argv[2], 'r') as fasta:
    for line in fasta:
        if line[0] == '>':
            item = line.strip().split()
            genename = item[0][1:]  
            info = transcripts[genename] 
            line = '>'+ genename + ' ' + ' '.join(info) + ' ' + item[-1] + '\n'
        file_out.write(line)
gff.close()
fasta.close()
file_out.close()