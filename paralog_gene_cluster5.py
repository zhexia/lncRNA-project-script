#我自己写的，还有bug,事实证明是大bug
import sys
import copy

genepairs_list = []
with open(sys.argv[1],'r') as f:
    for line in f:
        info = line.strip().split()
        gene1 = info[0]
        gene2 = info[1]
        gene_pair = {gene1, gene2}
        if (gene1 != gene2) and (gene_pair not in genepairs_list):
            genepairs_list.append(gene_pair)

genepairs_list_copy = copy.deepcopy(genepairs_list)
for genepair_copy in genepairs_list_copy:   
    geneA, geneB = genepair_copy
    geneA_fmy_index = -1
    geneB_fmy_index = -1
    i = 0
    for genepair in genepairs_list:
        if genepair_copy != genepair:
            if geneA in genepair:
                geneA_fmy_index = i 
            if geneB in genepair:
                geneB_fmy_index = i  
        i = i + 1  
    if ((geneA_fmy_index > -1) and (geneB_fmy_index > -1)) and (geneA_fmy_index != geneB_fmy_index):
        genepairs_list[geneA_fmy_index].update(genepairs_list[geneB_fmy_index])
        del genepairs_list[geneB_fmy_index]  
        if genepair_copy in genepairs_list:
            genepairs_list.remove(genepair_copy)             
    elif (geneA_fmy_index > -1) and (geneB_fmy_index == -1):
        genepairs_list[geneA_fmy_index].add(geneB)
        if genepair_copy in genepairs_list:
            genepairs_list.remove(genepair_copy)
    elif (geneB_fmy_index > -1) and (geneA_fmy_index == -1):
        genepairs_list[geneB_fmy_index].add(geneA)
        if genepair_copy in genepairs_list:
                genepairs_list.remove(genepair_copy)
lncrna_num = {}
with open(sys.argv[2],'r') as f:
    for line in f:
        info = line.split()
        num = int(info[1])
        key = info[0]
        lncrna_num[key] = num
family_ave_lncrna = lncrna_num[sys.argv[1].split('.')[0].split('/')[1]]/len(genepairs_list)

print('{} have {} genefamilys, family_ave_lncrna is {}'.format(sys.argv[1].split('.')[0].split('/')[1], len(genepairs_list),str('%.2f'%family_ave_lncrna)))