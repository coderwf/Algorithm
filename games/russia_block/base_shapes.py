
# -*- coding:utf-8 -*-
import random
import numpy as np

T_SHAPE = [[0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
           ]

O_SHAPE = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


Z_SHAPE = [[0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]]

S_SHAPE = [[0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]

J_SHAPE = [[0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

L_SHAPE = [[1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]

I_SHAPE = [[0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]]


SHAPES         = [T_SHAPE,O_SHAPE,S_SHAPE,L_SHAPE,I_SHAPE,J_SHAPE,Z_SHAPE]
SHAPES_NAMES   = ["T_SHAPE","O_SHAPE","S_SHAPE","L_SHAPE","I_SHAPE","J_SHAPE","Z_SHAPE"]

'''从SHAPES中随机选取一个作为自己的形状'''

class Shape(object):
    def __init__(self):
        index   = random.randint(0,len(SHAPES)-1)
        self.name = SHAPES_NAMES[index]
        shapes  = SHAPES[index]
        self.shapes = []
        for i in range(0,len(shapes)):
            shape  = np.array(shapes[i])
            shape.resize(4,4)
            self.shapes.append(shape)
        self.x =  0
        self.y =  0
        #任取一个形状作为初始形状
        self.count = random.randint(0,3)

    def change_shape(self):
        self.count = (self.count + 1) % 4

    def show(self):
        print self.name
        for shape in self.shapes:
            print shape

    #返回的是真实位置,相对于x和y的
    def get_blocks_pos_list(self):
        pos_list = []
        shape = self.shapes[self.count]
        for i in range(0,len(shape)):
            for j in range(0,len(shape[i])):
                if shape[i][j] == 1:
                    pos_list.append((self.x+j,self.y+i))
        return pos_list

    def get_shape(self):
        return self.shapes[self.count]

    #初始化自己相对于面板的位置
    def init_origin_pos(self,xs,ys):
        pass

    def set_xy(self,xy):
        self.x , self.y = xy

    def get_xy(self):
        return self.x,self.y

    def get_next_shape_block_pos_list(self):
        count = (self.count + 1) % 4
        pos_list = []
        shape = self.shapes[count]
        for i in range(0, len(shape)):
            for j in range(0, len(shape[i])):
                if shape[i][j] == 1:
                    pos_list.append((self.x + j, self.y + i))
        return pos_list


if __name__ == "__main__":
    shape = Shape()
    print shape.get_shape()
    print shape.get_blocks_pos_list()
    print shape.get_next_shape_block_pos_list()
