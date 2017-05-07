# -*- coding:utf-8 -*-

from node import Node
from numpy import random
from initNetwork import init_network
from drawPic import *

if __name__ == "__main__":

    number_of_node = 100        # 传感网络节点数量
    width = 1000                # 长
    height = 1000               # 高

    source_id = random.randint(0, number_of_node)           # 源节点
    nodes = init_network(number_of_node, width, height)     # 生成网络
    print "source node is: %d (%d,%d)" % (source_id, nodes[source_id].x, nodes[source_id].x)
    dest_id = []

    while len(dest_id) < number_of_node*0.1:
        x = random.randint(0, number_of_node)  # 目的节点
        if x != source_id and x not in dest_id:
            dest_id.append(x)
            print "dest node is: %d (%d,%d) " % (x, nodes[x].x, nodes[x].x)

    draw_map(nodes, source_id, dest_id)
    #draw_energy(nodes)

    # 对目的节点聚类



