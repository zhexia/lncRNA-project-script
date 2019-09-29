# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 21:21:27 2018

@author: 桑叶
"""
#input： .gff3(特点是ID不唯一)  output:  intron length

import sys
import gffutils
from collections import defaultdict
import os

path = os.getcwd()

num = -1
geneDict = {}
fn = gffutils.example_filename(path+'/'+sys.argv[1])
db = gffutils.create_db(fn, ":memory:", merge_strategy='create_unique', keep_order=True)
for geneline in db.features_of_type('gene'):
    geneid = geneline.id
    geneDict[geneid] = defaultdict(list)
    for mRNAline in db.children(geneid, featuretype='mRNA', order_by='start'):
        mRNAid = mRNAline.id
        for exonline in db.children(mRNAid, featuretype='exon', order_by='start'):
            num = num + 1
            info = str(exonline).split()
            geneDict[geneid][mRNAid].append((int(info[3]),int(info[4])))

sumlength = 0
for genekey,value in geneDict.items():
    for mRNAkey,exonloci in value.items(): 
        for locus in exonloci:
            if locus == exonloci[0]:
                index = locus[1]
            else:
                length = locus[0] - index - 1
                sumlength = sumlength + length
                index = locus[1]        
         
avelength = sumlength/num      
print(' '.join(sys.argv[1].split('_')[0:2])+' genome average intron length is: {}'.format('%.2f'%avelength))
    
    
    
    
    
    
    
    
    
    
    
    
    