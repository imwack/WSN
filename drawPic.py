# -*- coding:utf-8 -*-
from node import Node
import matplotlib.pyplot as plt


# 画传感网拓扑图
def draw_map(nodes, source, dest):
    x = []
    y = []
    for node in nodes:
        x.append(node.x)
        y.append(node.y)
    plt.figure(figsize=(8, 6))
    plt.title('Sensor Network')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(x, y, '.k')

    # source node
    plt.plot(source.x, source.y, 'r*')
    plt.annotate('Source', xy=(source.x, source.y),
                 xytext=(source.x+1, source.y+1))

    # dest node
    for d in dest:
        plt.plot(d.x, d.y, 'b*')
    return plt

# 画能量分布图
def draw_energy(nodes,energy0):
    e = []
    x = [n for n in range(0, len(nodes))]
    x2 = [n+0.2 for n in range(0, len(nodes))]
    for node in nodes:
        e.append(node.energy)

    #fig = plt.figure()
    plt.bar(x, e,  facecolor='lightskyblue', edgecolor='white')
    # width:柱的宽度
    plt.bar(x2 ,energy0,  facecolor='yellowgreen', edgecolor='white')

    print e
    print energy0
    sum = 0
    for i in range(len(e)):
        sum+= energy0[i]-e[i]
    print "energy:",sum
    plt.title('Node-Energy')
    plt.xlabel('Node')
    plt.ylabel('Energy')
    plt.show()


def draw_after_cluster(nodes, source, dest, cluster_center, dest_cluster):
    color = ['c', 'b', 'g', 'm', 'w', 'y', 'k', 'r', '#FF00FF', '#00FF00']
    x = []
    y = []
    for node in nodes:
        x.append(node.x)
        y.append(node.y)
    plt.figure(figsize=(8, 6))
    plt.title('Sensor Network')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.scatter(x, y, c='k', s=10, alpha=0.4, marker='o')

    # source node
    plt.scatter(source.x, source.y, c='r')
    plt.annotate('Source', xy=(source.x, source.y),
                 xytext=(source.x + 1, source.y + 1))
    # print dest_cluster
    for c in cluster_center:
        plt.scatter(c[0], c[1], c='r')
        plt.annotate('Center', xy=(c[0], c[1]),
                     xytext=(c[0] + 1, c[1] + 1))
    for i in range(len(dest)):
        pass
        plt.scatter(dest[i].x, dest[i].y, c=color[dest_cluster[i]])
    # plt.show()
    return plt
