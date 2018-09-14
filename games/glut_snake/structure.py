
# -*- coding:utf-8 -*-

'''实现一个队列存储蛇的身体的坐标位置'''
from games.glut_snake import define
#队列中的节点
class Node(object):
    def __init__(self,t,x = 0,y = 0):
        self.x     = x    #x坐标
        self.y     = y    #y坐标
        self.t     = t    #节点类别
        self.next  = None  #下一个节点
#链表队列
class Snake(object):
    def __init__(self):
        self.head = Node(0,0,0)   #头节点不存放任何信息
        self.head.next = None
        self.tail = self.head
        self.length = 0           #长度
    #放入一个node,从尾部插入
    def push_(self,node):
        self.tail.next = node
        self.tail      = node
        node.next      = None
        self.length    += 1
        
    #pop一个节点从头部pop
    def delete_tail(self):
        head_next = self.head.next
        if head_next == None:
            return
        self.head.next = head_next.next
        self.length    -= 1
        head_next.next = None
        return head_next
    
    def add_head(self,x,y):
        self.length += 1
        node = Node(define.SHEAD,x,y)
        self.push_(node)
        #print "add_head"
    
    def add_body(self,x,y):
        self.length += 1
        node = Node(define.SBODY,x, y)
        self.push_(node)
        #print "add_body"
        
    def get_head_pos(self):
        return self.tail.x,self.tail.y

    def __str__(self):
        text = "["
        head = self.head.next
        while head != None:
            text += "("+str(head.x) + ","+str(head.y)+")"
            head = head.next
        text += "]"
        return text