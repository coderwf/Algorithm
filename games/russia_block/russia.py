# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import numpy as np
import time
from games.russia_block import define
from games.russia_block import base_shapes

class Panel(object):
    def __init__(self,width,heitht):
        self.blocks = np.zeros((heitht,width),dtype=int)
        self.width = width
        self.height = heitht

    def get_value(self,x,y):
        return self.blocks[y][x]
    def set_value(self,x,y,value):
        self.blocks[y][x] = value
    def get_blocks(self):
        return self.blocks
    #判断是否一行都有方块
    def get_line_mode(self,y):
        all_false = True
        all_true  = True
        if y < 0:
            return define.LINEALLFALSE
        for j in range(0,self.width):
            if self.blocks[y][j] == 0:
                all_true = False
            elif self.blocks[y][j] == 1:
                all_false = False
        if all_true == True:
            return define.LINEALLTRUE
        if all_false == True:
            return define.LINEALLFALSE
        return define.LINEMIX

    def set_line_true(self,y,value):
        for j in range(0,self.width):
            self.blocks[y][j] = value

    def set_line_x_to_line_y(self,x,y):
        if x < 0:
            for j in range(0, self.width):
                self.blocks[y][j] = 0
            return
        for j in range(0,self.width):
            self.blocks[y][j] = self.blocks[x][j]

#横8个格子竖着12个格子
class russia(object):
    def __init__(self,w,xs=8,ys=16):
        pygame.init()
        pygame.display.set_caption("russian block")
        self.xs    = xs
        self.ys    = ys
        self.w     = w - w % self.xs
        self.size  = self.w / self.xs
        self.h     = self.size * self.ys
        self.o_x   = 20
        self.o_y   = 20
        self.screen   = pygame.display.set_mode((self.w+self.o_x*2,self.h+self.o_y*2))
        pygame.key.set_repeat(50)
        self.screen.fill(define.SPACE_COLOR)
        self.panel = Panel(self.xs,self.ys)
        self.shape    = None

    def get_shape(self):
        shape = base_shapes.Shape()
        self.brush_shape(shape.get_blocks_pos_list())
        pygame.display.flip()
        return shape

    #设置边界墙
    def set_wall(self,x,y,color=define.BLOCK_COLOR):
        x1 , y1 = x  ,y
        x2 , y2 = x + self.w +3, y1
        x3 , y3 = x , y + self.h + 3
        x4 , y4 = x + self.w+3  , y  + self.h + 3
        pygame.draw.line(self.screen,color, (x1, y1), (x2,y2) , 2)
        pygame.draw.line(self.screen,color, (x1, y1), (x3, y3), 2)
        pygame.draw.line(self.screen,color, (x2, y2), (x4, y4), 2)
        pygame.draw.line(self.screen,color, (x3, y3), (x4, y4), 2)

    #格子只是相对映射坐标,需要转换为真实像素点坐标
    def get_real_pos(self,x,y):
        return x * (self.size) + self.o_x , y * (self.size) +self.o_y

    #这个x y就是直接绘图的x y 绘图和擦除
    def erase_block(self,x,y):
        x, y = self.get_real_pos(x, y)
        pygame.draw.rect(self.screen, define.SPACE_COLOR, (x, y, self.size, self.size), 2)

    def brush_block(self,x,y,color = define.BLOCK_COLOR):
        x  , y  = self.get_real_pos(x,y)
        pygame.draw.rect(self.screen,color,(x,y,self.size,self.size), 2)
    def brush_shape(self,pos_list,color=define.BLOCK_COLOR):
        for pos in pos_list:
            x , y = pos
            self.brush_block(x,y,color)
    def erase_shape(self,pos_list):
        for pos in pos_list:
            x , y = pos
            self.erase_block(x,y)

    #检查碰撞,pos_list 中的是映射坐标 True表示碰撞了
    def check_coli(self,pos_list):
        for pos in pos_list:
            x , y = pos
            if x < 0 or x > (self.xs -1 ) or y < 0 or y > (self.ys-1):
                return True
            if self.panel.get_value(x,y) == 1:
                return True
        return False

    def get_key_down(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                yield define.KEYMAPS.get(event.key,define.UNDEFINED)

    #移动方块
    def move(self,direction):
        if direction == define.CHANGE:
            next_pos_list = self.shape.get_next_shape_block_pos_list()
            if self.check_coli(next_pos_list) == True:
                return define.EASYMOVE
            now_post_list = self.shape.get_blocks_pos_list()
            self.shape.change_shape()
            self.erase_shape(now_post_list)
            self.brush_shape(next_pos_list)
            pygame.display.flip()
            return define.EASYMOVE
        if direction == define.MOVEDOWN:
            now_pos_list = self.shape.get_blocks_pos_list()
            next_pos_list = []
            for pos in now_pos_list:
                next_pos = pos[0],pos[1] + 1
                next_pos_list.append(next_pos)
            #print now_pos_list,next_pos_list
            if self.check_coli(next_pos_list) == True:
                self.ensure_block(self.shape.get_blocks_pos_list())
                self.start_clear(self.shape)
                self.shape = self.get_shape()
                return define.MOVEDOWN
            self.erase_shape(now_pos_list)
            self.brush_shape(next_pos_list)
            x ,y = self.shape.get_xy()
            self.shape.set_xy((x,y+1))
            pygame.display.flip()
            return define.MOVEDOWN
        if direction == define.MOVELEFT:
            now_pos_list = self.shape.get_blocks_pos_list()
            next_pos_list = []
            for pos in now_pos_list:
                next_pos = pos[0] - 1, pos[1]
                next_pos_list.append(next_pos)
            #print now_pos_list, next_pos_list
            if self.check_coli(next_pos_list) == True:
                return define.EASYMOVE
            self.erase_shape(now_pos_list)
            self.brush_shape(next_pos_list)
            x, y = self.shape.get_xy()
            self.shape.set_xy((x - 1, y))
            pygame.display.flip()
            return define.EASYMOVE
        if direction == define.MOVERIGHT:
            now_pos_list = self.shape.get_blocks_pos_list()
            next_pos_list = []
            for pos in now_pos_list:
                next_pos = pos[0] + 1, pos[1]
                next_pos_list.append(next_pos)
            #print now_pos_list, next_pos_list
            if self.check_coli(next_pos_list) == True:
                return define.EASYMOVE
            self.erase_shape(now_pos_list)
            self.brush_shape(next_pos_list)
            x, y = self.shape.get_xy()
            self.shape.set_xy((x + 1, y))
            pygame.display.flip()
            return define.EASYMOVE

    #将方块值放入panel中表示这块有值了
    def ensure_block(self,pos_list):
        for pos in pos_list:
            x , y = pos
            self.panel.set_value(x,y,1)
    #包括start和line
    def rebrush_lines(self,start,end):
        while start <= end :
            for i in range(0,self.xs):
                if self.panel.get_value(i,start) == 1:
                    self.brush_block(i,start)
                else:
                    self.erase_block(i,start)
            start += 1
    #有方块到了底部所以需要判断是否要消去整行方块
    #先判断那几行是满的
    def start_clear(self,shape):
        pos_list = shape.get_blocks_pos_list()
        line_to_erase = []
        for pos in pos_list:
            if self.panel.get_line_mode(pos[1]) == define.LINEALLTRUE:
                line_to_erase.append(pos[1])
        if len(line_to_erase) == 0:
            return
        line_to_erase.sort(reverse=True)
        for y in line_to_erase:
            self.panel.set_line_true(y,0)
        start_line = line_to_erase[0] - 1
        off_set = 1
        while start_line >= 0 and self.panel.get_line_mode(start_line) != define.LINEALLFALSE:
            self.panel.set_line_x_to_line_y(start_line,start_line+off_set)
            start_line -= 1
        self.rebrush_lines(start_line,line_to_erase[0])
        pygame.display.flip()

    def start(self):
        self.set_wall(self.o_x-2, self.o_y-2, define.WALL_COLOR)
        self.shape = self.get_shape()
        pygame.display.flip()
        always = define.MOVEDOWN
        while True:
            t1 = time.time()
            res = define.EASYMOVE
            for direction in self.get_key_down():
                res = self.move(direction)
            if res == define.MOVEDOWN:
                time.sleep(0.3)
            else:
                t2 = time.time()
                time.sleep(0.3 - (t2-t1) / 1000.0)
            self.move(always)


if __name__ == "__main__":
    ru = russia(40)
    ru.start()
