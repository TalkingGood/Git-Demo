# -*- coding: gbk -*-
# �������

class Node:
    def __init__(self, value=None, left=None, rigth=None ):
        self.value=value
        self.left = left  #������
        self.rigth = rigth #������

#ǰ�����
def preTraverse(root):
    if root == None:
        return
    print(root.value, end=" ")
    preTraverse(root.left)
    preTraverse(root.rigth)

#�������
def midTraverse(root):
    if root == None:
        return
    midTraverse(root.left)
    print(root.value, end=" ")
    midTraverse(root.rigth)

#�������
def afterTravese(root):
    if root == None:
        return
    afterTravese(root.left)
    afterTravese(root.rigth)
    print(root.value, end=" ")

if __name__ == '__main__':
    print("��������������� ")
    root = Node('D', Node('B', Node('A'), Node('C')), Node('E',rigth= Node('G', Node('F'))))
    print('ǰ������� ')
    preTraverse(root)
    print('\n���������')
    midTraverse(root)
    print('\n���������')
    afterTravese(root)