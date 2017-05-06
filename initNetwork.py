# -*- coding:utf-8 -*-
from node import Node


def init_network(number_of_node=100, width=1000, height=1000, prt=0):

    nodes = []
    for i in range(number_of_node):
        node = Node(width, height)
        nodes.append(node)

    for i in range(number_of_node):
        if prt:
            print "%d:(%d,%d) %f" % (i, nodes[i].x, nodes[i].y, nodes[i].energy)

    print "_______init end__________"
    return nodes

