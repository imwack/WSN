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


def calc_next_step(nodes, source, pos):
    temp_node = nodes[:]
    print "dest:(%d,%d)" % (pos[0], pos[1])
    path = []  # 选择的路径
    p1 = 0.4
    p2 = 0.4
    p3 = 0.2
    ss = source
    for time in range(1, 100):
        # a = numpy.sqrt( pow(pos[0]-source.x,2) + pow(pos[1]-source.y,2) )
        degree = []  # 角度
        distance = []  # 距离
        energy = []  # 能量
        score = []  # 评分
        candidate = []  # 候选节点
        current_src = ss
        # source-dest:a  source-node:b  node-dest:c

        distanceToDest =  a = numpy.sqrt(pow(pos[0] - current_src.x, 2) + pow(pos[1] - current_src.y, 2))
        if distanceToDest<100:
            break

        for node in temp_node:
            if node.id == current_src.id:
                continue

            if node.energy < 1000:  # 能量过低舍去
                continue

            a = numpy.sqrt(pow(pos[0] - current_src.x, 2) + pow(pos[1] - current_src.y, 2))
            b = numpy.sqrt(pow(node.x - current_src.x, 2) + pow(node.y - current_src.y, 2))
            if b > numpy.sqrt(width * height) / 10:  # 距离过大直接舍去
                continue

            c = numpy.sqrt(pow(pos[0] - node.x, 2) + pow(pos[1] - node.y, 2))
            if c>a and c>b:
                continue
            cos = (a ** 2 + b ** 2 - c ** 2) / 2 / a / b
            # d = math.acos((a * a + c * c - b * b) / 2 / a / c) * 180 / math.pi  # 角度degree = a2+c2-b2/2ac
            d = math.acos(cos) * 180 / math.pi  # 角度degree = a2+c2-b2/2ac

            # if d<90:
            #     continue
            # dx1 = pos[0]*1.0  - current_src.x*1.0
            # dy1 = pos[1]*1.0 - current_src.y*1.0
            # dx2 = node.x*1.0 - current_src.x*1.0
            # dy2 = node.y*1.0 - current_src.y*1.0
            # zz = numpy.sqrt(dx1 * dx1 + dy1 * dy1) * numpy.sqrt(dx2 * dx2 + dy2 * dy2)
            # d = (dx1 * dx2 + dy1 * dy2) / zz
            # print d
            # d = abs(d*180/3.1415926)
            #break
            #d = math.acos((dx1 * dx2 + dy1 * dy2) / zz)

            distance.append(b)
            degree.append(d)
            energy.append(node.energy)
            candidate.append(node.id)


        #print degree
        min_distance = numpy.min(distance)
        max_distance = numpy.max(distance)

        distance = normalization(distance)
        degree = normalization(degree)
        energy = normalization(energy)
        score = p1 * distance + p2 * degree +p3/(energy+0.00000000001)  # 距离越小越好 角度越小越好 能量越大越好

        #　print candidate, score
        next_step = 1  # 最终选择的下一跳 分数最小的
        for i in range(len(score)):
            if score[i] < score[next_step]:
                next_step = i
        path.append(candidate[next_step])

        #print "next step id:", candidate[next_step],"len node:",len(temp_node)
        for node in temp_node:
            if node.id == candidate[next_step]:
                ss = node
        d = -1
        for i in range(len(temp_node)):
            if temp_node[i].id == candidate[next_step]:
                # 减少能量
                #temp_node[i].energy  -= 0.1*distance[next_step]
                dis = (max_distance+min_distance) * distance[next_step] + min_distance
                temp_node[i].energy -= (0.0001 * dis*dis + 0.05)*512
                d = i
                break
        if d!=-1:
            del temp_node[d]
            print d

    return path


if __name__ == "__main__":

    number_of_node = 1000        # 传感网络节点数量
    number_of_dest = 10
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

    energy0 = []    #初始能量
    for node in nodes:
        energy0.append(node.energy)
    #draw_energy(nodes,energy0)
    # 对目的节点聚类
    clf = cluster(dest,clusters)
    cluster_center = clf.cluster_centers_
    dest_cluster = clf.labels_              # 目标节点分类
    plt = draw_after_cluster(nodes, source, dest, cluster_center, dest_cluster)
    # plt.show()
    paths = []
    for pos in cluster_center:
        path = calc_next_step(nodes, source, pos)
        paths.append(path)

    print paths

    xx = []
    yy = []

    for i in range(len(paths)):
        x = [source.x]
        y = [source.y]
        path = paths[i]
        for id in path:
            x.append(nodes[id].x)
            y.append(nodes[id].y)
        x.append(cluster_center[i][0])
        y.append(cluster_center[i][1])
        xx.append(x)
        yy.append(y)

    color = ['c-', 'b-', 'g-', 'm-', 'w-', 'y-', 'k-', 'r-']
    for i in range(len(xx)):
        plt.plot(xx[i], yy[i], color[i])
    plt.show()

    draw_energy(nodes,energy0)
