# -*- coding:utf-8 -*-

from numpy import random
from sklearn.cluster import KMeans
from node import Node
from initNetwork import init_network,init_dest_node
from drawPic import *

if __name__ == "__main__":

    number_of_node = 100       # 传感网络节点数量
    number_of_dest = 10
    width = 1000                # 长
    height = 1000               # 高

    source_id = random.randint(0, number_of_node)           # 源节点
    nodes = init_network(number_of_node, width, height)     # 生成网络
    #print "source node is: %d (%d,%d)" % (source_id, nodes[source_id].x, nodes[source_id].x)
    dest_id = init_dest_node(nodes,number_of_dest,source_id,0)

    #draw_map(nodes, source_id, dest_id)
    #draw_energy(nodes)

    # 对目的节点聚类
    feature = []
    for id in dest_id:
        temp = []
        temp.append(nodes[id].x)
        temp.append(nodes[id].y)
        feature.append(temp)
    #print feature

    clf = KMeans(n_clusters=3)
    s = clf.fit(feature)
    cluster_center = clf.cluster_centers_
    cluster = clf.labels_



