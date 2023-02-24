# -*- coding: gbk -*-

print("铁轨列车出栈管理案例")

#(1) 创建Stack类，在类中创建判断栈内是否存在元素 in_empty()函数，进栈push()函数，出战pop()函数，取栈帝国函数gettop()函数
class Stack(object):
    def __init__(self):
        self.stack = []

    # 判断栈内是否存在元素
    def is_empty(self):
        return bool(self.stack)

    #进栈函数
    def push(self,data):
        self.stack.append(data)

    #出栈函数
    def pop(self):
        return self.stack.pop()

    #取栈顶元素函数
    def gettop(self):
        return self.stack[-1]


#添加实现本案例需要的参数，输入车厢个数及车厢出战的顺序，将出战顺序用字典存储
stack = Stack()
target = {}
C = {}
isOk = 1
A = 1 #A为进入的车厢编号
B = 1
n = int(input("请输入车厢个数："))
targetStr = input("请输入车厢出战的顺序： ").split(" ") #输入车厢出站的顺序
for index in range(0, len(targetStr) , 1):
    target[index + 1] = int(targetStr[index])

#利用循环判出站顺序是否能从A到B,如果能，isOk的值不变，否则变为0
while B <= n:
    if A == target[B]:  #判断进站车厢的编号与出站车厢的编号是否相同
        A += 1
        B += 1
    elif (int(stack.is_empty())!= 0) and (stack.gettop() == target[B]):#如果不同，判断栈顶与出站车厢编号是否相同
        stack.pop() #出站（出栈）
        B += 1 #对比车厢编号
    elif A <= n: #判断车厢是否全部进站
        stack.push(A)
        A += 1 #进站（进栈）
    else:
        isOk = 0

#输出是否能够实现此顺序
if isOk:
    print("能够出站")
else:
    print("不能出站")


