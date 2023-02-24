# -*- coding:gbk -*-
print("老鼠走迷宫")

#把一只老鼠放入迷宫中（输入起始位置）。迷宫以二维数组表示，0表示墙，1表示老鼠可以移动的路径。
#老鼠不能离开迷宫或者翻墙，从用户指定的位置开始移动,判断老鼠是否能走出迷宫


#（1）创建一个列表作为迷宫的地图
maze = [[1,1,0,1,0,1],
        [1,1,1,0,1,0],
        [0,0,1,0,1,0],
        [0,1,1,1,0,0],
        [0,0,0,1,1,0],
        [1,0,0,0,0,0]]

#(2)定义map,确保老鼠不会不会走出迷宫的范围并且判断当前这条路是否通畅
def map(maze, x, y):
    if (x >= 0 and x < len(maze)) and y >= 0 and y < len(maze[0]) and maze[x][y] == 1:
        return True
    else:
        return False

#(3)定义move()函数，功能一：用来判断老鼠是否走出迷宫。功能二：用来模拟来老鼠的行走路径。ps:为防止老鼠原路返回，将走过的路标记为2
#功能三：采用回溯发（即发现当前的候选解不可能时解时，就放弃它而选择下一个后按解），该方法用 递归的方案去实现
def move(maze, x, y):
    if(x == 0 and y == 0): #判断是否走到迷宫出口
        print("能够走出迷宫")
        return True
    if map(maze, x, y):
        maze[x][y] = 2 #防止原路返回
        #对四个方向进行试探，判断那个方向可以走---如果都不行则撤回
        if not move(maze, x - 1, y):
            maze[x][y] = 1
        elif not move(maze, x, y - 1):
            maze[x][y] = 1
        elif not move(maze, x + 1, y):
            maze[x][y] = 1
        elif not move(maze, x, y + 1):
            maze[x][y] = 1
        else:
            return False
    return True

a = int(input("输入起始位置的行坐标: "))
b = int(input("输入起始位置的列坐标: "))
move(maze, a, b)
#判断第0行和第1列 或者 第1行和第0列是否为1， 诺都为1说明未到达终点
if maze[0][1] == 1 and maze[1][0] == 1:
    print("走不出迷宫")



