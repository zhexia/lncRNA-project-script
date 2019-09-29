# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:28:59 2018

@author: chenw
"""
#符合要求就修改>后的名称，不符合要求的序列就丢掉。代码的优点在于边读边写，不需要数据结构存储，更快。

chrom_dict = {"NC_003070.9": "chr1", "NC_003071.7": "chr2", 
              "NC_003074.8": "chr3", "NC_003075.7": "chr4", 
              "NC_003076.8": "chr5"}

in_fa = open("Arabidopsis_thaliana_genome_raw.fa", 'r')
out_fa = open("Arabidopsis_thaliana_genome.fa", 'w')

flag = False
for line in in_fa:
    if line[0] == '>':
        chrom = line.strip().split(' ')[0][1:]
        if chrom in chrom_dict:
            chrom = chrom_dict[chrom]
            line = '>' + chrom + '\n'
            flag = True
        else:
            flag = False
    if flag:
        out_fa.write(line)
in_fa.close()
out_fa.close()