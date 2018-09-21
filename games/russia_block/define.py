
# -*- coding:utf-8 -*-

BLOCK_COLOR   =  (255,0,0)
SPACE_COLOR   = (255,255,255)
WALL_COLOR    = (0,0,0)


MOVEDOWN      = 200
MOVELEFT      = 201
MOVERIGHT     = 202


CHANGE       = 400
POUSE        = 401
QUIT         = 402

DOWNCOMPLETE = 500
MOVE         = 501
UNDEFINED    = 502
FLIP         = 503
DONOTHING    = 504
STARTERASE   = 505

KEYMAPS      = {
ord('w'):CHANGE,
ord('W'):CHANGE,
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

OPMAPS  ={
ord('w'):MOVE,
ord('W'):MOVE,
ord('a'):MOVE,
ord('A'):MOVE,
ord('s'):MOVE,
ord('S'):MOVE,
ord('d'):MOVE,
ord('p'):POUSE,
ord('P'):POUSE,
ord('q'):QUIT,
ord('Q'):QUIT,
}

EASYMOVE       = 100001
MOVEDOWNMOVE   = 100002
MOVEDOWNOK     = 100003

LINEALLFALSE   = 200000
LINEALLTRUE    = 200001
LINEMIX        = 200002

