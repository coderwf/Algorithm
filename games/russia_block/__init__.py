# -*- coding:utf-8 -*-

''''俄罗斯方块
每次下落或者改变位置都先擦除原来的位置然后给现在的位置上色
用一个大的矩阵列表来表示一个形状 0 1
矩阵中方块的位置是相对于整个大矩阵的位置
所有的位置都是映射位置 即 (0,0)代表(0,0)
(0,1) - (0,1*block_size)

所有的填充都是往上右填充
'''