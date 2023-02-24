# -*- coding: gbk -*-
print("股票收益最大化案例")

#定义 BestStock_n_time()函数，基于动态规划的思想，实现股票价格的差值

def BestStock_n_time(arr):
    len1 = len(arr)
    if len1 < 2:
        return 0
    diffArr = []   #股票价差值
    add_value = []
    for i in range(len1 -1):
        diffArr.append(arr[i+1] - arr[i])
    sum = 0 #股票最大收益
    for i in range(len(diffArr)):
        if diffArr[i] > 0 :
            add_value.append(diffArr[i])
            sum += diffArr[i]
    return diffArr, add_value , sum

if __name__ == '__main__':
    try:
        while True:
            print("股票价格： ", end='')
            arr = [int(i) for i in input().split()]
            diffArr, add_value, sum = BestStock_n_time(arr)
            print("股票价差值：" ,diffArr)
            print("股票增值数：", add_value)
            print("股票最大收益：{}".format(sum))
    except:
        pass