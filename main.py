# -*- coding:utf-8 -*-

from node import Node
from initNetwork import init_network
from drawPic import *

if __name__ == "__main__":

    number_of_node = 100
    width = 1000    # 长
    height = 1000   # 高
    nodes = init_network(number_of_node, width, height)     # 生成网络
    draw_map(nodes)
    draw_energy(nodes)


