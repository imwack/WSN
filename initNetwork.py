# -*- coding:utf-8 -*-
from node import Node
from numpy import random

'''
生成网络
arg: 结点数，x范围，y范围
prt: 是否打印网络
'''
def init_network(number_of_node=100, width=1000, height=1000, prt=0):

    nodes = []
    for i in range(number_of_node):
        node = Node(width, height)
        nodes.append(node)

    for i in range(number_of_node):
        if prt:
            print "%d:(%d,%d) %f" % (i, nodes[i].x, nodes[i].y, nodes[i].energy)

    # print "_______init end__________"
    return nodes

# 生成目的节点
def init_dest_node(nodes, number_of_dest, source_id, prt=0):
    dest_id = []
    number_of_node = len(nodes)
    while len(dest_id) < number_of_dest:
        x = random.randint(0, number_of_node)
        if x != source_id and x not in dest_id:
            dest_id.append(x)
            if prt:
                print "dest node is: %d (%d,%d) " % (x, nodes[x].x, nodes[x].y)
    return dest_id


