#coding=gbk
print("下落的树叶案例")
#(1)创建坐标轴，存储每个水平位置的节点的权值之和
axis = [0 for i in range(100)] #创建100个元素的坐标轴axis,存储每个水平位置节点的权值之和
print("按先序遍历方式输入此二叉树:")

#(2)创建tree（）函数，输入节点数据，若为-1则返回上一级，使用递归实现每个水平点的位置相加
def tree(pos):
    x = int(input()) #输入数据
    if x == -1:
        return
    axis[pos] += x #对定位的坐标节点求权值之和
    tree(pos - 1)
    tree(pos + 1)

#(3) 以中点作为递归起点，调用递归tree()函数实现。若axis保存的值大于0，则将各个值输出
tree(50)
print("输入结果为：",end=' ')
for x in axis:
    if x > 0 :
        print(x, end=' ')
