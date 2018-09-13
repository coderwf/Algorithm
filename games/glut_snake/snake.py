# -*- coding:utf-8 -*-
from games.glut_snake.structure import Queue
import pygame
from games.glut_snake import define
from pygame.locals import *
from sys import exit
import numpy as np
import random
from games.glut_snake import structure

'''面板大小和方块大小同等比例缩放
容纳20个方块'''

class Grass(object):
    # 活动范围大小
    def __init__(self, size=500):
        self.size = size        #活动范围
        self.max_x = 20         #网格最大数
        self.o_x = 20           #活动范围起始xy位置
        self.o_y = 20
        size = size - size % self.max_x  # 取整数
        self.s_size = size / self.max_x  # 每块大小
        self.blocks = np.zeros((self.max_x,self.max_x),dtype=int) #所有网格的标记
        self.snake , self.food = self.init_snake_and_food()
        pygame.init()
        pygame.display.set_caption("glutt snake ")
        self.screen = pygame.display.set_mode((self.size + self.o_x * 2, self.size + self.o_y * 2))
        # print self.screen
        # 先初始化蛇的身体和食物

    def init_snake_and_food(self):
        snake   = Queue()
        x = random.randint(1, 18)
        y = random.randint(1, 18)
        snake.push(x,y,define.SHEAD)
        self.blocks[x][y] = define.SHEAD
        ra = random.randint(0, 3)
        if ra == 0:
            x1 = x + 1
            y1 = y
        elif ra == 1:
            x1 = x
            y1 = y + 1
        elif ra == 2:
            x1 = x
            y1 = y - 1
        else:
            x1 = x - 1
            y1 = y
        snake.push(x1, y1, define.SBODY)
        self.blocks[x1][y1] = define.SBODY
        return snake,self.get_food()

    def get_food(self):
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        while self.blocks[x][y] != define.SPACE:
            x = random.randint(0, 19)
            y = random.randint(0, 19)
        self.blocks[x][y] = define.FOOD
        print "food", x, y
        return structure.Node(define.FOOD,x,y)

    # 由方格子位置得到实际位置
    def __get_real_pos__(self, x, y):
        x1 = x * self.s_size + self.o_x + 2
        y1 = y * self.s_size + self.o_y + 2
        return x1, y1

    # 第一次画食物和蛇
    def draw_snake_and_food(self):
        head = self.snake.head.next
        print head.x, head.y
        self.draw_head(head.x,head.y)
        head = head.next
        while head != None:
            #print head.x,head.y
            self.draw_body(head.x, head.y)
            head = head.next
        self.draw_food(self.food.x, self.food.y)

    #获取当前长度
    def get_snake_length(self):
        return self.queue.length

    def draw_head(self, x, y, color=define.RED):
        x, y = self.__get_real_pos__(x, y)
        pygame.draw.rect(self.screen, color, Rect(x, y, self.s_size, self.s_size))

    def draw_body(self, x, y, color=define.BODYCOLOR):
        x, y = self.__get_real_pos__(x, y)
        pygame.draw.rect(self.screen, color, Rect(x, y, self.s_size, self.s_size))

    def draw_food(self, x, y, color=define.FOODCOLOR):
        x,y = self.__get_real_pos__(x,y)
        pygame.draw.rect(self.screen,color,Rect(x,y,self.s_size,self.s_size))

    def erase_block(self, x, y):
        x, y = self.__get_real_pos__(x, y)
        pygame.draw.rect(self.screen, define.WHITE,Rect(x,y,self.s_size,self.s_size))

    # 设置背景色
    def set_bk(self, color=define.WHITE):
        self.screen.fill(color)

    # 绘画墙壁
    def set_wall(self, ):
        origin_x = self.o_x
        origin_y = self.o_y
        height = self.size + 2
        width = self.size  + 2
        pygame.draw.line(self.screen, define.BLACK, (origin_x, origin_y), (width + origin_x, origin_y), 2)
        pygame.draw.line(self.screen, define.BLACK, (origin_x, origin_y), (origin_x, height + origin_y), 2)
        pygame.draw.line(self.screen, define.BLACK, (origin_x, origin_y + height),
                         (origin_x + width, height + origin_y), 2)
        pygame.draw.line(self.screen, define.BLACK, (origin_x + width, origin_y + height), (origin_x + width, origin_y),
                    2)

    def process_keydown(self,key):
        x , y = self.snake.get_head_pos()
        next_x,next_y = x, y
        if key == ord('w') or key == ord('W'):
            next_x = x
            next_y = y - 1
        elif key == ord('a') or key == ord('A'):
            next_x = x - 1
            next_y = y
        elif key == ord('s') or key == ord('S'):
            next_x = x
            next_y = y + 1
        elif key == ord('d') or key == ord('D'):
            next_x = x + 1
            next_y = y
        if next_x > 19 or next_x < 0:
            return 0
        if next_y > 19 or next_y < 0:
            return 0
        if self.blocks[next_x][next_y] == define.SBODY:
            return 0
        if self.blocks[next_x][next_y] == define.SPACE:
            self.blocks[x][y] = define.SBODY
            self.blocks[next_x][next_y] = define.SHEAD
            node = self.snake.pop()
            self.blocks[node.x][node.y] = define.SPACE
            self.snake.push(next_x,next_y,define.SHEAD)
            self.draw_head(next_x,next_y)
            self.draw_body(x,y)
            self.erase_block(node.x,node.y)
            return 1
        if self.blocks[next_x][next_y] == define.FOOD:
            self.blocks[x][y] = define.SBODY
            self.blocks[next_x][next_y] = define.SHEAD
            self.snake.push(next_x,next_y)
            self.draw_body(x,y)
            self.draw_head(next_x,next_y)
            self.food = self.get_food()
            print self.food.x , self.food.y
            self.draw_food(self.food.x , self.food.y)

    def quit(self):
        pygame.quit()

    def start(self):
        char = 'w'
        self.set_bk()
        self.set_wall()
        self.draw_snake_and_food()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    char = ord(event.key)
                res = self.process_keydown(char)
                if res == 0:
                    pygame.quit()
                pygame.display.flip()

if __name__ == "__main__":
    grass = Grass()
    grass.start()