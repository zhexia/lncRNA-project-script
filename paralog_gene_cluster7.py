genepairs_list = [{'l','k'},{8,9},{0,3},{'d','t'},{8,6},{8,0},{'l',0},{'p',9},{'u',99},{'o','l'},{88,'t'},{'p',0},{'f','u'},{'y','p'},{'p','l'}]
genepairs_list=[{1,2},{2,3},{1,4},{1,99},{5,6}]
empty = set()
for genepairs1 in genepairs_list:
    print(genepairs1)
    print('====================')
    is_match = 0
    for genepairs2 in genepairs_list:
        print(genepairs2)
        if genepairs2 != empty and genepairs1 != genepairs2 and genepairs1 & genepairs2:
            is_match += 1
            genepairs1 |= genepairs2
            genepairs_list.remove(genepairs2)
    print('====================')
    if is_match:
        genepairs_list.insert(0, empty)

final = [i for i in genepairs_list if len(i) != 0]
print(final)
