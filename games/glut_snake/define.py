
# -*-coding:utf-8 -*-

'''一些定义信息'''

SHEAD   = 2         #蛇头
SBODY   = 1         #蛇身体
WALL    = -1        #墙壁
FOOD    = -2        #食物
SPACE   = 0         #空白处


WHITE      = (255,255,255)
BLACK      = (0,0,0)
RED        = (255,0,0)
BODYCOLOR  = (51,133,255)
FOODCOLOR  = (118,182,26)

FAILED     = 202
DONOTHING  = 200
CONTINUE   = 201
MOVE       = 203

QUIT       = 100
POUSE      = 101
MOVEUP     = 102
MOVEDOWN   = 103
MOVERIGHT  = 104
MOVELEFT   = 105
UNDEFINED  = 106

map = {ord('w'):MOVEUP,
       ord('W'):MOVEUP,
ord('a'):MOVELEFT,
ord('A'):MOVELEFT,
ord('s'):MOVEDOWN,
ord('S'):MOVEDOWN,
ord('d'):MOVERIGHT,
ord('D'):MOVERIGHT,
ord('p'):POUSE,
ord('P'):POUSE,
ord('q'):QUIT,
ord('Q'):QUIT,
       }

REVERT_DIRE = {
    MOVELEFT:MOVERIGHT,
    MOVERIGHT:MOVELEFT,
    MOVEDOWN:MOVEUP,
    MOVEUP:MOVEDOWN
}


DIRE_EXPLAIN = {
    MOVEDOWN:"move down",
    MOVEUP:"move up",
    MOVERIGHT:"move right",
    MOVELEFT:"move left",
}