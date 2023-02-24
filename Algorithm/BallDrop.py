#coding=gbk
import math
print("小球下落案例")
#(1) 计算总节点个数，定义reverseRes()函数，实现开关状态的噶便
D = 4 # 二叉树深度
I = int(input("请输入下落小球的个数： ")) #下落小球的个数
n = int(round((math.pow(2,D)) - 1)) #2^D -1 ,所有节点个数
s = {} #每个节点的开关状态
def reverseRes(num):
    if num == 1:
        return 0
    elif num == 0:
        return 1
#(2)初始化所有开关状态为OFF
for index in range(1, n+1, 1): #初始化所有开关
    s[index] = 0 # 所有开关都关闭

#（3）遍历每个小球，当小球经过对应节点时，改变节点开关状态，通过开关状态判断当前小球下落的方向，直到小球下落到最后的叶子节点
for index in range(1, I+1, 1): #遍历每个小球
    k = 1 #需要一个辅助的编号，因为小球每次都是从第一个开关经过
    while 1:
        s[k] = reverseRes(s[k]) #改变节点开关状态
        if s[k] == 1: #小球经过以后，开关打开了，说明经过之前是闭合的，所以往左走
            k = 2 * k
        else:
            k = 2 * k + 1
        if k > n:
            break
print("最后一个小球将会落到：{0}".format(int(k/2)))
