# -*- coding: gbk -*-
import random

#(1) ����confict()���������»ʺ����㣬���ʺ�ڷŵ�λ���Ƿ�Ϲ�
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True

    return False

#����queens�����������������ķ�ʽ��ȷ��ÿһ���ʺ��λ�ã����õݹ�ʵ����һ���ʺ��λ�á�conflict���������ж����޳�ͻ�����û�г�ͻ��
#�������ǰ�ʺ��λ������
def queens(num = 8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1 :
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

#��3������prettyprint()�������� ��*�� ��ʾ�ʺ��λ�ã�ͨ�������ķ�ʽ��ʾ�������
def prettyprint(solution):
    def line(pos, length = len(solution)):
        return '0 ' * pos + '* ' + '0 ' * (length - pos -1)
    for pos in solution:
        print(line(pos))

#(4)�õ��˻ʺ�����ȫ����ĸ��������������prettyprint()������ʾʽ��������н�
print('8�ʺ����⣬��%d�ֽ�' %(len(list(queens(8)))))
for ii in range(6):
    print(' ��%d�ֽ⣺' %(ii))
    prettyprint(random.choice(list(queens(8))))