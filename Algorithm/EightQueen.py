# -*- coding: gbk -*-
import random

#(1) 定义confict()函数传入新皇后的落点，看皇后摆放的位置是否合规
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True

    return False

#创建queens函数，采用生成器的方式来确定每一个皇后的位置，并用递归实现下一个皇后的位置。conflict（）函数判断有无冲突，如果没有冲突，
#则产生当前皇后的位置信心
def queens(num = 8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1 :
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

#（3）创建prettyprint()函数，用 “*” 表示皇后的位置，通过遍历的方式显示地输出解
def prettyprint(solution):
    def line(pos, length = len(solution)):
        return '0 ' * pos + '* ' + '0 ' * (length - pos -1)
    for pos in solution:
        print(line(pos))

#(4)得到八皇后问题全部解的个数并输出，调用prettyprint()函数显示式地输出所有解
print('8皇后问题，共%d种解' %(len(list(queens(8)))))
for ii in range(6):
    print(' 第%d种解：' %(ii))
    prettyprint(random.choice(list(queens(8))))