#参数1：过滤后的某个被比对物种的所有cluster的文件

import sys
import os
from collections import defaultdict

path=os.getcwd()
if not os.path.exists(path):
    os.makedirs(path)

cluster_dict = defaultdict(list)
with open(sys.argv[1], 'r') as f1:
    for line in f1:
        info = line.split() 
        if info[0].isdigit():
            key = info[0]
        else:
            if info[0] not in key:
                key = key + ' ' + info[0] + ' ' + info[1]       
            cluster_dict[key].append(line)



'''parent_num = 0
with open(sys.argv[1], 'r') as f1:
    for line in f1:
        gtf_list = []
        info = line.split()
        gtf_list.append(info[1])
        gtf_list.append('.')
        gtf_list.append('exon')
        if info[0].isdigit():
            exon_num = 0
            parent_num = parent_num + 1            
        else:
            parent = 'rna' + str(parent_num)
            exon_num = exon_num + 1
            start = info[8]
            end = info[9]
            strand = '+'
            if int(start) > int(end):
                start = info[9]
                end = info[8]
                strand = '-'
            
            ID = info[1] + ' ' + parent + ' ' + 'exon' + str(exon_num) + ' ' + start + ' ' + end
            gtf_list.append(start)
            gtf_list.append(end)
            gtf_list.append('.')
            gtf_list.append(strand)
            gtf_list.append('.')
            gtf_list.append('ID=' + ID)
            gtf_list.append('parent=' + parent)
            with open(path + '/' + sys.argv[1].split('.')[0] + '.gtf', 'a+') as f2:
                f2.write('\t'.join(gtf_list[:-2]) + '\t' + ';'.join(gtf_list[-2:]) + ';' + '\n')
f1.close()
f2.close()'''
