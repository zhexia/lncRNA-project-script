#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:36:44 2018

@author: zhangxuan
"""

network = [{'l','k'},{8,9},{0,3},{'d','t'},{8,6},{8,0},{'l',0},{'p',9},{'u',99},{'o','l'},{88,'t'}]

net_dict = dict()

for a,b in network:
    net_dict.setdefault(a, {})
    net_dict.setdefault(b, {})
    net_dict[a][b] = net_dict[b][a] = 0

    
nodes_dict = dict()

for node, links in net_dict.items():
    nodes_dict[node]=len(links.keys())

cluster = []
sorted_nodes_dict = sorted(nodes_dict.items(),key=lambda x:x[1], reverse=True)
nodes = [x[0] for x in sorted_nodes_dict]

num = 0

while(nodes):
    num += 1
    top_node = nodes[0]
    childs = list(net_dict[top_node].keys())
    fathers = set()
    fathers.add(top_node)
    while(childs):
        new_childs = childs
        for i in childs:
            print('.',end='')
            fathers.add(i)
            if nodes_dict[i]-1 == 0:
                new_childs.remove(i)
            else:
                new_childs.remove(i)
                childs_childs = set(net_dict[i].keys()) - fathers
                new_childs = set(new_childs) | childs_childs
        childs = list(new_childs)
    cluster.append(fathers)
    print('cluster {}'.format(num), fathers)
    for i in fathers:
        nodes.remove(i)

print(cluster)
    