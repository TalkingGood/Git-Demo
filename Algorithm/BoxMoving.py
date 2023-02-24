# -*- coding: gbk -*-
print("盒子移动案例")

#创建空列表并为列表中的盒子编号，输出盒子编号
Num = int(input("请输入盒子的个数："))
list = []
for i in range(1, Num + 1):
    list.append(i)

print("盒子编号为：", list)


#用def定义move()函数，表示小球的移动。定义order列表，用于存放盒子移动的命令编号和X,Y的盒子编号
def move(list):
    order = []
    order.append(int(input("移动命令：")))
    order.append(int(input("X的盒子编号：")))
    order.append(int(input("Y的盒子编号：")))
    #根据order[0]值的大小，执行相应的操作。当值为1时，将盒子X置于盒子Y的左边，当值为2时，将盒子X置于盒子Y的右边
    #当值为3时，交换盒子X和盒子Y的位置；当值为4时，倒置位表
    if order[0] == 1:
        item = list.pop(order[1] - 1)
        list.insert(order[2] -2 , item)
    if order[0] == 2:
        item = list.pop(order[1] - 1)
        list.insert(order[2] - 1 , item)
    if order[0] == 3:
        list[order[2] - 1],list[order[1] - 1] = list[order[[1] - 1] - 1],list[order[2] - 1]
    if order[0] == 4:
        list.reverse()
    return list

#循环十次
for i in range(1, 10):
    move_list = move(list)
    print('第', i , '次移动后：', move_list)

