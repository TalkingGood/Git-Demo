# -*- coding: gbk -*-
print("��Ʊ������󻯰���")

#���� BestStock_n_time()���������ڶ�̬�滮��˼�룬ʵ�ֹ�Ʊ�۸�Ĳ�ֵ

def BestStock_n_time(arr):
    len1 = len(arr)
    if len1 < 2:
        return 0
    diffArr = []   #��Ʊ�۲�ֵ
    add_value = []
    for i in range(len1 -1):
        diffArr.append(arr[i+1] - arr[i])
    sum = 0 #��Ʊ�������
    for i in range(len(diffArr)):
        if diffArr[i] > 0 :
            add_value.append(diffArr[i])
            sum += diffArr[i]
    return diffArr, add_value , sum

if __name__ == '__main__':
    try:
        while True:
            print("��Ʊ�۸� ", end='')
            arr = [int(i) for i in input().split()]
            diffArr, add_value, sum = BestStock_n_time(arr)
            print("��Ʊ�۲�ֵ��" ,diffArr)
            print("��Ʊ��ֵ����", add_value)
            print("��Ʊ������棺{}".format(sum))
    except:
        pass