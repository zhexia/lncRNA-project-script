# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 21:38:37 2018

@author: chenw
"""

def parse_blast(A2B_blast_file, B2A_blast_file):
    A2B_set = set()
    with open(A2B_blast_file, 'r') as A2B_blast:
        for line in A2B_blast:
            item = line.strip().split('\t')
            gene1, gene2 = item[:2]
            A2B_set.add(gene1 + '\t' + gene2)
    B2A_set = set()
    with open(B2A_blast_file, 'r') as B2A_blast:
        for line in B2A_blast:
            item = line.strip().split('\t')
            gene2, gene1 = item[:2]
            B2A_set.add(gene1 + '\t' + gene2)
    A_B_set = A2B_set & A2B_set
    A_to_B_list = list()
    for A_B in A_B_set:
        A_to_B_list.append(set(A_B.split('\t')))
    return A_to_B_list


    
        
    