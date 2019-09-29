# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:21:54 2018

@author: chenw
"""


blast_result = open("Arabidopsis_thaliana_lncRNA_to_Arabidopsis_thaliana_genome.blast", 'r')

lncRNA_dict = dict()
for line in blast_result:
    lncRNA, chrom = line.strip().split('\t')[:2]
    start = int(line.strip().split('\t')[8])
    end = int(line.strip().split('\t')[9])
    strand = '+'
    if start > end:
        strand = '-'
        tmp = start
        start = end
        end = tmp
        
    if lncRNA in lncRNA_dict:
        if chrom in lncRNA_dict[lncRNA]:
            if strand in lncRNA_dict[lncRNA][chrom]:
                lncRNA_dict[lncRNA][chrom][strand].append([start, end])
            else:
                lncRNA_dict[lncRNA][chrom][strand] = [[start, end]]
        else:
            lncRNA_dict[lncRNA][chrom] = dict()
            lncRNA_dict[lncRNA][chrom][strand] = [[start, end]]
    else:
        lncRNA_dict[lncRNA] = dict()
        lncRNA_dict[lncRNA][chrom] = dict()
        lncRNA_dict[lncRNA][chrom][strand] = [[start, end]]    

blast_result.close()


def blocks_to_locis(blocks, gap):
    locis = [[],]
    index = 0
    start = blocks[0][0]
    end = 0
    for block in sorted(blocks):
        end = block[0]
        dist = end - start
        if dist < gap:
            locis[index].append(block)
        else:
            index = index + 1
            locis.append([block])
        start = block[1]
    return locis

    
'''blocks_to_locis
blocks = [[1,4], [8, 10], [300,320], [400, 420]]
gap = 50
blocks_to_locis(blocks, gap)
'''
                
lncRNA_transcript_dict = dict()
for lncRNA in lncRNA_dict:
    for chrom in lncRNA_dict[lncRNA]:
        for strand in lncRNA_dict[lncRNA][chrom]:
            exons = lncRNA_dict[lncRNA][chrom][strand]
            exons = sorted(exons, key=lambda x:x[0])
                           
            transcripts = blocks_to_locis(exons, 10000)
            
            transcripts_num = len(transcripts)
            if lncRNA in lncRNA_transcript_dict:
                lncRNA_transcript_dict[lncRNA] += transcripts_num
            else:
                lncRNA_transcript_dict[lncRNA] = 0
                lncRNA_transcript_dict[lncRNA] += transcripts_num

macth_num_list = [0, 0, 0, 0, 0, 0]
for lncRNA in lncRNA_transcript_dict:
    if lncRNA_transcript_dict[lncRNA] == 1:
        macth_num_list[0] += 1
    elif lncRNA_transcript_dict[lncRNA] == 2:
        macth_num_list[1] += 1
    elif lncRNA_transcript_dict[lncRNA] == 3:
        macth_num_list[2] += 1
    elif lncRNA_transcript_dict[lncRNA] == 4:
        macth_num_list[3] += 1
    elif lncRNA_transcript_dict[lncRNA] == 5:
        macth_num_list[4] += 1
    else:
        macth_num_list[5] += 1 

print(macth_num_list)