# -*- coding:utf-8 -*-

import numpy
import math
from numpy import random
from sklearn.cluster import KMeans
from node import Node
from initNetwork import init_network,init_dest_node
from drawPic import *

if __name__ == "__main__":

    number_of_node = 100       # 传感网络节点数量
    number_of_dest = 10
    clusters = 3                #类别个数
    width = 1000                # 长
    height = 1000               # 高

    nodes = init_network(number_of_node, width, height)     # 生成网络
    source = nodes[0]           # 源节点
    dest = nodes[-10:]          # 目的节点
    nodes = nodes[1:-10]
    #print "source node is: (%d,%d)" % (source.x, source.y)

    #draw_map(nodes, source, dest)
    #draw_energy(nodes)

    # 对目的节点聚类
    feature = []
    for id in dest:
        temp = []
        temp.append(id.x)
        temp.append(id.y)
        feature.append(temp)
    #print feature

    clf = KMeans(n_clusters=clusters)
    s = clf.fit(feature)
    cluster_center = clf.cluster_centers_
    dest_cluster = clf.labels_              #目标节点分类
    #draw_after_cluster(nodes, source, dest, dest_cluster)

    #source-dest:a  source-node:b  node-dest:c
    #degree = a2+c2-b2/2ac
    for pos in cluster_center:
        a = numpy.sqrt( pow(pos[0]-source.x,2) + pow(pos[1]-source.y,2) )
        degree = []
        for node in nodes:
            b = numpy.sqrt( pow(node.x-source.x,2) + pow(node.y-source.y,2) )
            if b>numpy.sqrt(width*height)/2:
                continue
            c = numpy.sqrt( pow(pos[0]-node.x,2) + pow(pos[1]-node.y,2) )
            cos = (a**2+c**2-b**2)/2/a/c
            print cos
            d = math.acos((a**2+c**2-b**2)/2/a/c)   #角度


