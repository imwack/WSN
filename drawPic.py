# -*- coding:utf-8 -*-
from node import Node
import matplotlib.pyplot as plt


# 画传感网拓扑图
def draw_map(nodes, source_id, dest_id):
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
    plt.plot(nodes[source_id].x, nodes[source_id].y, 'r*')
    plt.annotate('Source', xy=(nodes[source_id].x, nodes[source_id].y),
                 xytext=(nodes[source_id].x+1, nodes[source_id].y+1))

    # dest node
    for x in dest_id:
        plt.plot(nodes[x].x, nodes[x].y, 'b*')
    plt.show()


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



