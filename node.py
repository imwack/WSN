# -*- coding:utf-8 -*-

from numpy import random


'''
无限传感网络节点类
坐标(x,y)
能量energy
'''


class Node(object):
    id = 0
    x = 0
    y = 0
    energy = 0.0
    '''构造函数'''
    def __init__(self, width=1000, height=1000):
        self.x = random.randint(1, width)   # [1,width]
        self.y = random.randint(1, height)  # [1,height]
        self.energy =float( random.randint(500,10000) )
        #self.energy = random.rand()         # [0,1]浮点数

