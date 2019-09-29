# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:11:00 2018

@author: 桑叶
"""
#参数1：lncRNAname_cluster_coverage?.txt文件  伪参数2(不用跟在.py文件后)：lncRNAname_cluster_coverage.txt(通过 参数1.split('.')[0][:-2] + '.txt' 来实现，注意，因为lncRNAname_cluster_coverage?.txt和lncRNAname_cluster_coverage.txt在同一个目录下才可以这样搞) 
#输出lncRNAname_cluster_coverage?_new.txt文件

#读取lncRNAname_cluster_coverage?.txt和lncRNAname_cluster_coverage.txt，保留lncRNAname_cluster_coverage.txt中lncRNAname_cluster_coverage?.txt里有的clusters.这一步是因为lncRNAname_cluster_coverage?.txt中过滤出来的clusters的信息不全，下一步分析需要过滤出来的clusers信息全
import sys
import os

path=os.getcwd()
if not os.path.exists(path):
    os.makedirs(path)
 
cov30_list = []
with open(sys.argv[1], 'r') as f1:
    for line in f1:
        info = line.split()
        numorder = info[0]
        cov30_list.append(numorder) 
cluster_Dict = {}
with open(sys.argv[1].split('.t')[0][:-2] + '.txt', 'r') as f2:
    for line in f2:
        if line[:2] != '\n':
            info = line.split()
            if info[0].isdigit():
                key = info[0]
                cluster_Dict[key] = []
            else:
                if line[0] != 'c':
                    cluster_Dict[key].append(line)
                else:
                    cluster_Dict[key+' '+ line.strip()] = cluster_Dict[key]
                    del cluster_Dict[key]

f_out = open(path + '/' + sys.argv[1].split('.')[0] + '_new.txt', 'a+')
for key,value in cluster_Dict.items():
        if key.split()[0] in cov30_list: 
            f_out.write(key + ' ' + '-*140\n' + ''.join(value[0:]))
f1.close()
f2.close() 
f_out.close()          


        

        