# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit
import numpy as np
import random
import time
from games.russia_block import shape
from games.russia_block import define
#横8个格子竖着12个格子
class russia(object):
    def __init__(self,w):
        pygame.init()
        pygame.display.set_caption("russian block")
        self.xs    = 8
        self.ys    = 12
        self.w     = w - w % self.xs
        self.size  = self.w / self.xs
        self.h     = self.size * 12
        self.o_x   = 20
        self.o_y   = 20
        self.screen   = pygame.display.set_mode((self.w+self.o_x*2,self.h+self.o_y*2))
        self.screen.fill(define.SPACE_COLOR)
        self.blocks   = np.zeros((self.h,self.w),dtype=int) #每次方块固定落地以后才会改变值
        self.shape    = None
        print self.w , self.size

    def set_wall(self,x,y,color):
        x1 , y1 = x  ,y
        x2 , y2 = x + self.w +3, y1
        x3 , y3 = x , y + self.h + 3
        x4 , y4 = x + self.w+3  , y  + self.h + 3
        pygame.draw.line(self.screen,color, (x1, y1), (x2,y2) , 2)
        pygame.draw.line(self.screen,color, (x1, y1), (x3, y3), 2)
        pygame.draw.line(self.screen,color, (x2, y2), (x4, y4), 2)
        pygame.draw.line(self.screen,color, (x3, y3), (x4, y4), 2)

    def get_shape(self):
        index = random.randint(0,len(shape.shapes)-1)
        s     = shape.shapes[index]

    def brush_shape(self,x,y,mat,color=define.BLOCK_COLOR):
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                if mat[j][i] == 1:
                    print "brush"
                    self.brush_block(x+j,i+y,color)

    def erase_shape(self,x,y,mat):
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                if mat[j][i] == 1:
                    self.erase_block(x+j,i+y,color)

    def get_real_pos(self,x,y):
        return x * (self.size) + self.o_x , y * (self.size) +self.o_y

    def erase_block(self,x,y):
        x, y = self.get_real_pos(x, y)
        pygame.draw.rect(self.screen, define.SPACE_COLOR, (x, y, self.size, self.size), 2)

    def brush_block(self,x,y,color):
        x  , y  = self.get_real_pos(x,y)
        pygame.draw.rect(self.screen,color,(x,y,self.size,self.size), 2)

    def check_left_coli(self,x,y,mat):
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                if mat[j][i] == 0:
                    continue
                rx , ry = j+x,i+y
                if rx < 0 or self.blocks[ry][rx] == 1:
                    return False
        return True

    def check_right_coli(self,x,y,mat):
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                if mat[j][i] == 0:
                    continue
                rx , ry = j+x,i+y
                if rx  >(self.xs-1) or self.blocks[ry][rx] == 1:
                    return False
        return True
    def check_down_coli(self,x,y,mat):
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                if mat[j][i] == 0:
                    continue
                rx , ry = j+x,i+y
                if ry  >(self.ys-1) or self.blocks[ry][rx] == 1:
                    return False
        return True

    def check_coli(self,x,y,mat):
        pass

    def change_shape(self,sha):
        return sha.change_shape()

    def get_key_down(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                print event.type
                yield event.key

    def pouse(self):
        for key in self.get_key_down():
            if define.OPMAPS.get(key) == define.POUSE:
                return

    def move(self,key):
        direction = define.KEYMAPS.get(key)
        if direction == define.CHANGE:
            mat = self.shape.get_change() #得到改变形状后的矩阵列表
            if self.check_coli(self.shape.x,self.shape.y,mat) == True:
                return define.DONOTHING
            self.erase_shape(self.shape.x,self.shape.y,self.shape.mat)
            self.brush_shape(self.shape.x,self.shape.y,mat)
            self.shape.change_shape()
            return define.FLIP
        if direction == define.MOVEDOWN:
            mat = self.shape.get_mat()
            if self.check_down_coli(self.shape.x,self.shape.y+1,mat) == True:
                return define.DONOTHING
            self.erase_shape(self.shape.x, self.shape.y, mat)
            self.brush_shape(self.shape.x, self.shape.y+1, mat)
            self.shape.y += 1
            return define.DOWNCOMPLETE
        if direction == define.MOVERIGHT:
            mat = self.shape.get_mat()
            if self.check_down_coli(self.shape.x + 1, self.shape.y , mat) == True:
                return define.DONOTHING
            self.erase_shape(self.shape.x, self.shape.y, mat)
            self.brush_shape(self.shape.x + 1, self.shape.y + 1, mat)
            self.shape.x += 1
            return define.FLIP
        if direction == define.MOVELEFT:
            mat = self.shape.get_mat()
            if self.check_down_coli(self.shape.x - 2, self.shape.y, mat) == True:
                return define.DONOTHING
            self.erase_shape(self.shape.x, self.shape.y, mat)
            self.brush_shape(self.shape.x -1, self.shape.y, mat)
            self.shape.x -= 1
            return define.FLIP

    def test(self):
        Z_shape = shape.Z_shape()
        print Z_shape.mat
        self.brush_shape(3,4,Z_shape.mat,define.BLOCK_COLOR)
        pygame.display.flip()

    def start(self):
        self.set_wall(self.o_x-2, self.o_y-2, define.WALL_COLOR)
        pygame.display.flip()
        always = define.MOVEDOWN
        self.test()
        while True:
            res = define.DONOTHING
            for key in self.get_key_down():
                print key


if __name__ == "__main__":
    ru = russia(400)
    ru.start()
