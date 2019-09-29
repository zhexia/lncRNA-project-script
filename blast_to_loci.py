# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:27:59 2018

@author: chenw
"""

def exons_to_transcripts(exons, gap):
    transcripts = list()
    if len(exons) == 1:
        transcripts = [exons]
        return transcripts
    else:
        transcript = list()        
        front_exon = exons[0]
        transcript.append(front_exon)
        exons = exons[1:]
        back_exon = exons[0]
        dist = back_exon[0] - front_exon[1]
        while dist < gap:
            transcript.append(back_exon)
            exons = exons[1:]
            if len(exons) > 0:                
                front_exon = back_exon
                back_exon = exons[0]
                dist = back_exon[0] - front_exon[1]
            else:
                break
        transcripts = [transcript]
        if len(exons) > 0:
            transcripts.extend(exons_to_transcripts(exons, gap))
            return transcripts
        else:
            return transcripts
            
exons = [[1,4], [8, 10], [300,320], [400, 420]]
gap = 50
print(exons_to_transcripts(exons, gap))
