# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:27:59 2018

@author: sangye
"""
def cluster_exons(exon_list,gap):
    cluster_dict = {}
    index = -gap 
    num = 0
    for loci in sorted(exon_list):                                      
        if int(loci[0]) > index+gap:
            num = num + 1
            cluster_dict['cluster'+str(num)] = []
        cluster_dict['cluster'+str(num)].append(loci)    
        index = loci[0]
    return cluster_dict
print(cluster_exons([[1,4],[9,14],[78,90]],50))
