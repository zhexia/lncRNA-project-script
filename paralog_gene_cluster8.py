# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 19:17:26 2018

@author: chenw
"""

import sys
sys.setrecursionlimit(10000000)

input_file_name = "Zea_mays_lncrnas.blast"
output_file_name = "Zea_mays_lncrnas_module.txt"

input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

node_state = dict()
network = dict()
for line in input_file:
    nodeA, nodeB = line.strip().split('\t')[:2]
    if nodeA == nodeB:
        continue
    node_state[nodeA] = 0
    node_state[nodeB] = 0    
    if nodeA in network:
        network[nodeA].add(nodeB)
    else:
        network[nodeA] = set()
        network[nodeA].add(nodeB)
    if nodeB in network:
        network[nodeB].add(nodeA)
    else:
        network[nodeB] = set()
        network[nodeB].add(nodeA)

# 定义深度优先搜索函数，一般是一个递归函数
def dfs(node, node_state, network):
    module = set()
    if (node_state[node] == 0): # 如果没有被访问过，则递归访问
        module.update(network[node])
        node_state[node] = 1 # 标记为访问过
        for neighbor in network[node]:
            module.update(dfs(neighbor, node_state, network))
    return module

for node in node_state:
    if (node_state[node] == 0):
        module = dfs(node, node_state, network)
        for node_ in module:
            output_file.write(node_ + ';')
        output_file.write('\n')   
 
input_file.close()
output_file.close()

