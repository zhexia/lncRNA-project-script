# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:44:07 2018

@author: chenw
"""

import re

transcripts = dict()
with open('Arabidopsis_thaliana_TAIR10.1_genomic.gff', 'r') as gff:
        for line in gff:
            if line[0] == '#':
                continue
            item = line.strip().split('\t')
            if item[2] == "exon":
                try:
                    transcript_id = re.findall('transcript_id=([^;]*)', item[8])[0]
                    start = int(item[3])
                    end = int(item[4])
                    if transcript_id in transcripts:
                        transcripts[transcript_id].append(start)
                        transcripts[transcript_id].append(end)
                    else:
                        transcripts[transcript_id] = list()
                        transcripts[transcript_id].append(start)
                        transcripts[transcript_id].append(end)
                except:
                    pass

intron_num = 0
intron_len_sum = 0 
for transcript_id in transcripts:
    position = transcripts[transcript_id]
    position.sort()
    if len(position) > 2:
        for i in range(2, len(position), 2):
            intron_len = position[i] - position[i - 1]
            intron_num = intron_num + 1
            intron_len_sum = intron_len_sum + intron_len

print(intron_len_sum / intron_num)
