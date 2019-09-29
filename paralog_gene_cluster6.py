import copy
genepairs_list = [{'l','k'},{8,9},{0,3},{'d','t'},{8,6},{8,0},{'l',0},{'p',9},{'u',99},{'o','l'},{88,'t'}]
genepairs_list=[{1,2},{2,3},{1,4},{5,6}]
genepairs_list_copy = copy.deepcopy(genepairs_list)

empty = set()

for genepairs in genepairs_list:
    is_match = 0
    #print(genepairs)
    for genepairs_copy in genepairs_list_copy:
        print(genepairs_copy)
        if genepairs_copy != empty and genepairs_copy != genepairs and genepairs & genepairs_copy:
            is_match += 1
            genepairs |= genepairs_copy
            genepairs_list.remove(genepairs_copy)
    if is_match:
        genepairs_list.insert(0, empty)
    genepairs_list_copy = copy.deepcopy(genepairs_list)

final = [i for i in genepairs_list if len(i) != 0]
print(final)
