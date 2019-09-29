genepairs_list = [{'l','k'},{8,9},{0,3},{'d','t'},{8,6},{8,0},{'l',0},{'p',9},{'u',99},{'o','l'},{88,'t'}]
gene_set = {'l', 'k', 8, 9, 0, 3, 'd', 't', 6, 'p', 'u', 99, 'o', 88}

for gene in gene_set:
    index_list = list()
    for genepair in genepairs_list:
        if gene in genepair:
            index_list.append(genepairs_list.index(genepair))
    
    first_index = index_list[0]
    for i in range(1, len(index_list)):
        index = index_list[i] - i + 1
        genepairs_list[first_index].update(genepairs_list[index])
        del genepairs_list[index]
print(genepairs_list)


