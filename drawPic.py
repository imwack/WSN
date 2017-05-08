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
    plt.show()
    return plt

# 画能量分布图
def draw_energy(nodes):
    e = []
    x = [n for n in range(0, len(nodes))]
    for node in nodes:
        e.append(node.energy)

    fig = plt.figure()
    plt.bar(x, e, alpha=0.5, color='g')

    plt.title('Node-Energy')
    plt.xlabel('Node')
    plt.ylabel('Energy')
    plt.show()

def draw_after_cluster(nodes, source, dest, dest_cluster):
    plt = draw_map(nodes, source, dest)


