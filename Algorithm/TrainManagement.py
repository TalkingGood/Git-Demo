# -*- coding: gbk -*-

print("�����г���ջ������")

#(1) ����Stack�࣬�����д����ж�ջ���Ƿ����Ԫ�� in_empty()��������ջpush()��������սpop()������ȡջ�۹�����gettop()����
class Stack(object):
    def __init__(self):
        self.stack = []

    # �ж�ջ���Ƿ����Ԫ��
    def is_empty(self):
        return bool(self.stack)

    #��ջ����
    def push(self,data):
        self.stack.append(data)

    #��ջ����
    def pop(self):
        return self.stack.pop()

    #ȡջ��Ԫ�غ���
    def gettop(self):
        return self.stack[-1]


#���ʵ�ֱ�������Ҫ�Ĳ��������복������������ս��˳�򣬽���ս˳�����ֵ�洢
stack = Stack()
target = {}
C = {}
isOk = 1
A = 1 #AΪ����ĳ�����
B = 1
n = int(input("�����복�������"))
targetStr = input("�����복���ս��˳�� ").split(" ") #���복���վ��˳��
for index in range(0, len(targetStr) , 1):
    target[index + 1] = int(targetStr[index])

#����ѭ���г�վ˳���Ƿ��ܴ�A��B,����ܣ�isOk��ֵ���䣬�����Ϊ0
while B <= n:
    if A == target[B]:  #�жϽ�վ����ı�����վ����ı���Ƿ���ͬ
        A += 1
        B += 1
    elif (int(stack.is_empty())!= 0) and (stack.gettop() == target[B]):#�����ͬ���ж�ջ�����վ�������Ƿ���ͬ
        stack.pop() #��վ����ջ��
        B += 1 #�Աȳ�����
    elif A <= n: #�жϳ����Ƿ�ȫ����վ
        stack.push(A)
        A += 1 #��վ����ջ��
    else:
        isOk = 0

#����Ƿ��ܹ�ʵ�ִ�˳��
if isOk:
    print("�ܹ���վ")
else:
    print("���ܳ�վ")


