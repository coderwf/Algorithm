
# -*- coding:utf-8 -*-
''''所有的形状'''
import numpy as np
from abc import abstractmethod
import random
class shape(object):
    def __init__(self):
        self.mat1 = np.zeros((4,4),dtype=int)
        self.mat2 = np.zeros((4,4),dtype=int)
        self.mat3 = np.zeros((4,4),dtype=int)
        self.mat4 = np.zeros((4,4),dtype=int)
        self.mats = [self.mat1,self.mat2,self.mat3,self.mat4]
        self.count = random.randint(0,3)
        self.init_shape()
        self.mat  = self.mats[self.count]
        self.x    = 0
        self.y    = 0  #整个矩阵的位置
    @abstractmethod
    def init_shape(self):
        pass
    def change_shape(self):
        old = self.mat
        self.count = (self.count + 1) % 4
        self.mat   = self.mats[self.count]
        return old,self.mat
    def get_mat(self):
        return self.mat

    def process_pos(self,w,h):
        pass
    def show_(self):
        print self.mat1
        print self.mat2
        print self.mat3
        print self.mat4
    def get_most_left(self):
        pass
    def get_most_right(self):
        pass
    def get_most_top(self):
        pass
class I_shape(shape):
    def init_shape(self):
        self.mat1[0][1] = 1
        self.mat1[1][1] = 1
        self.mat1[2][1] = 1
        self.mat1[3][1] = 1
        self.mat2[2][0] = 1
        self.mat2[2][1] = 1
        self.mat2[2][2] = 1
        self.mat2[2][3] = 1
        self.mat3[0][2] = 1
        self.mat3[1][2] = 1
        self.mat3[2][2] = 1
        self.mat3[3][2] = 1
        self.mat4[1][0] = 1
        self.mat4[1][1] = 1
        self.mat4[1][2] = 1
        self.mat4[1][3] = 1

    def show(self):
        print "I shape"
        self.show_()
class Z_shape(shape):
    def init_shape(self):
        self.mat1[0][1] = 1
        self.mat1[1][0] = 1
        self.mat1[1][1] = 1
        self.mat1[2][0] = 1
        self.mat2[1][1] = 1
        self.mat2[1][2] = 1
        self.mat2[2][1] = 1
        self.mat2[2][0] = 1
        self.mat3[0][1] = 1
        self.mat3[1][1] = 1
        self.mat3[1][2] = 1
        self.mat3[2][2] = 1
        self.mat4[0][1] = 1
        self.mat4[1][1] = 1
        self.mat4[1][0] = 1
        self.mat4[0][2] = 1
    def show(self):
        print "Z shape"
        self.show_()
class L_shape(shape):
    def init_shape(self):
        self.mat1[0][0] = 1
        self.mat1[0][1] = 1
        self.mat1[1][1] = 1
        self.mat1[2][1] = 1
        self.mat2[1][0] = 1
        self.mat2[1][1] = 1
        self.mat2[1][2] = 1
        self.mat2[2][0] = 1
        self.mat3[0][1] = 1
        self.mat3[1][1] = 1
        self.mat3[2][1] = 1
        self.mat3[2][2] = 1
        self.mat4[1][0] = 1
        self.mat4[1][1] = 1
        self.mat4[1][2] = 1
        self.mat4[0][2] = 1
    def show(self):
        print "L shape"
        self.show_()
class J_shape(shape):
    def init_shape(self):
        self.mat1[0][1] = 1
        self.mat1[1][0] = 1
        self.mat1[1][1] = 1
        self.mat1[2][0] = 1
        self.mat2[1][0] = 1
        self.mat2[1][1] = 1
        self.mat2[2][1] = 1
        self.mat2[2][2] = 1
        self.mat3[0][1] = 1
        self.mat3[1][1] = 1
        self.mat3[1][2] = 1
        self.mat3[2][2] = 1
        self.mat4[0][0] = 1
        self.mat4[0][1] = 1
        self.mat4[1][1] = 1
        self.mat4[1][2] = 1
    def show(self):
        print "J shape"
        self.show_()

class T_shape(shape):
    def init_shape(self):
        self.mat1[1][0] = 1
        self.mat1[0][1] = 1
        self.mat1[1][1] = 1
        self.mat1[2][1] = 1
        self.mat2[1][0] = 1
        self.mat2[1][1] = 1
        self.mat2[1][2] = 1
        self.mat2[2][1] = 1
        self.mat3[0][1] = 1
        self.mat3[1][1] = 1
        self.mat3[2][1] = 1
        self.mat3[1][2] = 1
        self.mat4[1][0] = 1
        self.mat4[1][1] = 1
        self.mat4[1][2] = 1
        self.mat4[0][1] = 1
    def show(self):
        print "T shape"
        self.show_()

class O_shape(shape):
    def init_shape(self):
        self.mat1[1][0] = 1
        self.mat1[2][0] = 1
        self.mat1[1][1] = 1
        self.mat1[2][1] = 1
        self.mat2 = self.mat1
        self.mat3 = self.mat1
        self.mat4 = self.mat1

    def show(self):
        print "O shape"
        self.show_()

class S_shape(shape):
    def init_shape(self):
        self.mat1[0][1] = 1
        self.mat1[1][1] = 1
        self.mat1[2][1] = 1
        self.mat1[2][0] = 1
        self.mat2[1][0] = 1
        self.mat2[1][1] = 1
        self.mat2[1][2] = 1
        self.mat2[2][2] = 1
        self.mat3[0][1] = 1
        self.mat3[0][2] = 1
        self.mat3[1][1] = 1
        self.mat3[2][1] = 1
        self.mat4[0][2] = 1
        self.mat4[1][0] = 1
        self.mat4[1][1] = 1
        self.mat4[1][2] = 1
    def show(self):
        print "S shape"
        self.show_()

#所有的形状
shapes = [T_shape,O_shape,S_shape,S_shape,J_shape,L_shape,I_shape]

if __name__ == "__main__":
    i_shape = Z_shape()
    print i_shape.get__most_left(0,0,i_shape.get_mat())
    print i_shape.mat