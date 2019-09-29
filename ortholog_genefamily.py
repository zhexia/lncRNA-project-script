# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 20:40:15 2018

@author: sangye
"""
#循环遍历blast_uniq_result目录下的文件，并进行处理得到ortholog gene familys
#注意：运行时已经将blast_uniq_result中物种自己比自己的结果删除了。例如Zma_to_Zea_mays_lncrnas_uniq.blast

import sys
import os
from collections import defaultdict

AB = defaultdict(list)
work_dir = os.getcwd()
for root, dirs, files in os.walk(work_dir):
    for f1 in files:
        for f2 in files:
            if (f1[0:3] == f2.split('_')[2][0] + f2.split('_')[3][0:2]) and (f2[0:3] == f1.split('_')[2][0] + f1.split('_')[3][0:2]):  
                A_to_B = []
                B_to_A = []
                with open (f1,'r') as f:
                    for line in f:
                        info = line.split()
                        st = set((info[1], info[2])) 
                        A_to_B.append(st)

                with open (f2,'r') as f:
                    for line in f:
                        info = line.split()
                        st = set((info[1], info[2])) 
                        B_to_A.append(st)

                for i in A_to_B:
                    if i in B_to_A:
                        keyname = f1[0:3] + '_to_' + f2[0:3]
                        AB[keyname].append(i)
gene_family_argv = AB.pop('Ath_to_Bna')
geneprs_argv = []
for key,value in AB.items():
    geneprs_argv = geneprs_argv + value

expand_gene_family(gene_family_argv, geneprs_argv)

# gene_family gene_pairs [{gene1,gene3}, {gene2,gene3}]
def expand_gene_family(gene_fmys, geneprs):
    for genepr in geneprs:
        geneA, geneB = genepr
        geneA_fmy_index = -1
        geneB_fmy_index = -1
        i = 0
        for gene_fmy in gene_fmys:
            if geneA in gene_fmy:
                geneA_fmy_index = i
            if geneB in gene_fmy:
                geneB_fmy_index = i
            i += 1
        if (geneA_fmy_index > -1) and (geneB_fmy_index > -1):
            gene_fmys[geneA_fmy_index].update(gene_fmys[geneB_fmy_index])
            del gene_fmys[geneB_fmy_index]
        elif (geneA_fmy_index > -1) and (geneB_fmy_index == -1):
            gene_fmys[geneA_fmy_index].add(geneB)
        elif (geneB_fmy_index > -1) and (geneA_fmy_index == -1):
            gene_fmys[geneB_fmy_index].add(geneA)
        else:
            gene_fmys.append(genepr)
    print('There are {} ortholog gene familys'.format(len(gene_fmys)))
    print(gene_fmys)