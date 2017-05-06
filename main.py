# -*- coding:utf-8 -*-

from node import Node


if __name__ == "__main__":

    number_of_node = 100
    width = 1000    # 长
    height = 1000   # 高
    nodes = []
    for i in range(number_of_node):
        node = Node(width,height)
        nodes.append(node)

    for i in range(number_of_node):
        print "%d:(%d,%d) %f" %(i,nodes[i].x,nodes[i].y,nodes[i].energy)
