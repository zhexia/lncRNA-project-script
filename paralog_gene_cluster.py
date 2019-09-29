#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 23:59:48 2018

@author: zhangxuan
"""

network = [{'l','k'},{8,9},{0,3},{'d','t'},{8,6},{8,0},{'l',0},{'p',9},{'u',99},{'o','l'},{88,'t'}]

def find_cluster(network, cluster, num):
    for i in range(1,len(network)):
        if len(network[0] & network[i]) >= 1:
            new_first = network[0] | network[i]
            del network[i]
            new_network = [new_first] + network[1:]
            if len(new_network) == 1:
                num += 1
                print('Cluster {}'.format(num), new_first)
                cluster.append(new_first)
                return cluster
            else:
                return find_cluster(new_network, cluster, num)
        else:
            print('.', end='')
            if i == len(network) - 1:
                num += 1
                print('Cluster {}'.format(num), network[0])
                cluster.append(network[0])
                if len(network[1:]) == 1:
                    num += 1
                    print('Cluster {}'.format(num), network[1])
                    cluster.append(network[1])
                    return cluster
                return find_cluster(network[1:], cluster, num)
        
cluster_result = find_cluster(network, cluster=[], num=0)
print(cluster_result)