# -*- coding:utf-8 -*-

import numpy
import math
from numpy import random
from sklearn.cluster import KMeans
from node import Node
from initNetwork import init_network,init_dest_node
from drawPic import *


# 归一化
def normalization(arr):
    amin, amax = numpy.min(arr), numpy.max(arr)  # 求最大最小值
    arr = (arr - amin) / (amax - amin)  # (矩阵元素-最小值)/(最大值-最小值)
    return arr


# 对目的节点聚类
def cluster(dest,clusters):
    feature = []
    for id in dest:
        temp = []
        temp.append(id.x)
        temp.append(id.y)
        feature.append(temp)
    # print feature
    clf = KMeans(n_clusters=clusters)
    s = clf.fit(feature)
    return clf


def calc_next_step(nodes, current_src, ):
    # a = numpy.sqrt( pow(pos[0]-source.x,2) + pow(pos[1]-source.y,2) )
    degree = []  # 角度
    distance = []  # 距离
    energy = []  # 能量
    score = []  # 评分
    candidate = []  # 候选节点
    path = []  # 选择的路径
    current_src = source
    # source-dest:a  source-node:b  node-dest:c
    for node in nodes:
        if node.energy < 0.1:  # 能量过低舍去
            continue

        a = numpy.sqrt(pow(pos[0] - current_src.x, 2) + pow(pos[1] - current_src.y, 2))
        b = numpy.sqrt(pow(node.x - current_src.x, 2) + pow(node.y - current_src.y, 2))
        if b > numpy.sqrt(width * height) / 2:  # 距离过大直接舍去
            continue

        c = numpy.sqrt(pow(pos[0] - node.x, 2) + pow(pos[1] - node.y, 2))
        cos = (a ** 2 + c ** 2 - b ** 2) / 2 / a / c
        d = math.acos((a * a + c * c - b * b) / 2 / a / c) * 180 / math.pi  # 角度degree = a2+c2-b2/2ac
        if d > 90:  # 角度过大舍去
            continue

        distance.append(b)
        degree.append(d)
        energy.append(node.energy)
        candidate.append(node.id)

    distance = normalization(distance)
    degree = normalization(degree)
    energy = normalization(energy)
    score = (0.5 * distance + 0.5 * degree) / (energy + 0.0000001)  # 距离越小越好 角度越小越好 能量越大越好
    # print score
    next_step = 1  # 最终选择的下一跳
    for i in range(len(score)):
        if score[i] < score[next_step]:
            next_step = i
    path.append(candidate[next_step])
    print "next step:%d (%d,%d)" % (candidate[next_step], nodes[candidate[next_step]].x, nodes[candidate[next_step]].y)


if __name__ == "__main__":

    number_of_node = 1000        # 传感网络节点数量
    number_of_dest = 100
    clusters = 3                # 类别个数
    width = 1000                # 长
    height = 1000               # 高

    nodes = init_network(number_of_node, width, height)     # 生成网络
    source = nodes[0]                       # 源节点 默认为第一个
    dest = nodes[-number_of_dest:]          # 目的节点 默认最后n个
    nodes = nodes[1:-number_of_dest]
    for i in range(0, len(nodes)):
        nodes[i].id = i
    # plt = draw_map(nodes, source, dest)
    # draw_energy(nodes)

    # 对目的节点聚类
    clf = cluster(dest,clusters)
    cluster_center = clf.cluster_centers_
    dest_cluster = clf.labels_              # 目标节点分类
    draw_after_cluster(nodes, source, dest, cluster_center, dest_cluster)

    paths = []
    for pos in cluster_center:
        # a = numpy.sqrt( pow(pos[0]-source.x,2) + pow(pos[1]-source.y,2) )
        degree = []     # 角度
        distance = []   # 距离
        energy = []     # 能量
        score = []      # 评分
        candidate = []  # 候选节点
        path = []       # 选择的路径
        current_src = source
        # source-dest:a  source-node:b  node-dest:c
        for node in nodes:
            if node.energy < 0.1:                # 能量过低舍去
                continue

            a = numpy.sqrt(pow(pos[0] - current_src.x, 2) + pow(pos[1] - current_src.y, 2))
            b = numpy.sqrt(pow(node.x-current_src.x, 2) + pow(node.y-current_src.y, 2))
            if b > numpy.sqrt(width*height)/2:    # 距离过大直接舍去
                continue

            c = numpy.sqrt(pow(pos[0]-node.x, 2) + pow(pos[1]-node.y, 2))
            cos = (a**2+c**2-b**2)/2/a/c
            d = math.acos((a*a+c*c-b*b)/2/a/c) * 180 / math.pi  # 角度degree = a2+c2-b2/2ac
            if d > 90:                            # 角度过大舍去
                continue

            distance.append(b)
            degree.append(d)
            energy.append(node.energy)
            candidate.append(node.id)

        distance = normalization(distance)
        degree = normalization(degree)
        energy = normalization(energy)
        score = (0.5*distance+0.5*degree)/(energy+0.0000001)         # 距离越小越好 角度越小越好 能量越大越好
        #print score
        next_step = 1  # 最终选择的下一跳
        for i in range(len(score)):
            if score[i] < score[next_step]:
                next_step = i
        path.append(candidate[next_step])
        print "next step:%d (%d,%d)" % (candidate[next_step], nodes[candidate[next_step]].x, nodes[candidate[next_step]].y)
        # print distance
        # print degree
        # print energy
