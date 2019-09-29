#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 08:53:42 2018

@author: zhangxuan
"""

network = [{'l','k'},{8,9},{0,3},{'d','t'},{8,6},{8,0},{'l',0},{'p',9},{'u',99},{'o','l'},{88,'t'}]

def find_cluster(network, cluster, num):
    ismatch = 0
    removeable = []
    new_first = network[0]
    for i in range(1,len(network)):
        print('.', end='')
        if len(network[0] & network[i]) >= 1:
            ismatch += 1
            new_first = new_first | network[i]
            removeable.append(network[i])
    if len(removeable):
        for r in removeable:
            network.remove(r)
        if len(network) == 1:
            cluster.append(new_first)
            return cluster
        else:
            new_network = [new_first] + network[1:]
            return find_cluster(new_network, cluster, num)
    else:
        num += 1
        print('Cluster {}'.format(num), new_first)
        cluster.append(new_first)
        if len(network[1:])==1:
            num += 1
            print('Cluster {}'.format(num), network[1])
            cluster.append(network[1])
            return cluster
        else:
            return find_cluster(network[1:], cluster, num)

cluster_result = find_cluster(network, cluster=[], num=0)
print(cluster_result)