# -*- coding: gbk -*-
# 二叉遍历

class Node:
    def __init__(self, value=None, left=None, rigth=None ):
        self.value=value
        self.left = left  #左子树
        self.rigth = rigth #右子树

#前序遍历
def preTraverse(root):
    if root == None:
        return
    print(root.value, end=" ")
    preTraverse(root.left)
    preTraverse(root.rigth)

#中序遍历
def midTraverse(root):
    if root == None:
        return
    midTraverse(root.left)
    print(root.value, end=" ")
    midTraverse(root.rigth)

#后序遍历
def afterTravese(root):
    if root == None:
        return
    afterTravese(root.left)
    afterTravese(root.rigth)
    print(root.value, end=" ")

if __name__ == '__main__':
    print("二叉遍历树案例： ")
    root = Node('D', Node('B', Node('A'), Node('C')), Node('E',rigth= Node('G', Node('F'))))
    print('前序遍历： ')
    preTraverse(root)
    print('\n中序遍历：')
    midTraverse(root)
    print('\n后序遍历：')
    afterTravese(root)