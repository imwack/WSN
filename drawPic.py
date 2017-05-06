# -*- coding:utf-8 -*-
from node import Node
import matplotlib.pyplot as plt


def draw_map(nodes):
    x = []
    y = []
    for node in nodes:
        x.append(node.x)
        y.append(node.y)
    plt.figure(figsize=(8, 6))
    plt.title('Sensor Network')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(x, y, '.')
    plt.show()


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



