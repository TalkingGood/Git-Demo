# -*- coding: gbk -*-
print("�����ƶ�����")

#�������б�Ϊ�б��еĺ��ӱ�ţ�������ӱ��
Num = int(input("��������ӵĸ�����"))
list = []
for i in range(1, Num + 1):
    list.append(i)

print("���ӱ��Ϊ��", list)


#��def����move()��������ʾС����ƶ�������order�б����ڴ�ź����ƶ��������ź�X,Y�ĺ��ӱ��
def move(list):
    order = []
    order.append(int(input("�ƶ����")))
    order.append(int(input("X�ĺ��ӱ�ţ�")))
    order.append(int(input("Y�ĺ��ӱ�ţ�")))
    #����order[0]ֵ�Ĵ�С��ִ����Ӧ�Ĳ�������ֵΪ1ʱ��������X���ں���Y����ߣ���ֵΪ2ʱ��������X���ں���Y���ұ�
    #��ֵΪ3ʱ����������X�ͺ���Y��λ�ã���ֵΪ4ʱ������λ��
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

#ѭ��ʮ��
for i in range(1, 10):
    move_list = move(list)
    print('��', i , '���ƶ���', move_list)

