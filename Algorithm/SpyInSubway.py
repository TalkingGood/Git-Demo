#coding=gbk
import numpy as np

print("地铁里的间谍案例")
#（1）导入numpy包，用[i][j]表示时刻i,在车站j最少还要等待多长时间
has_train = np.zeros((100,100,2))
dp = np.zeros((100,100)) #dp[i][j]表示时刻i，在车站j最少还要等待多长时间

#（2）输入地铁站个数n，会见时刻T,各站到下一站的行驶时间,M1,M1列车出发时间,M2,M2列车出发时间等
n = int(input("请输入地铁站个数n:"))
T = int(input("请输入会见时刻T:"))
t = [0]
t1 = [0] * (100 - n)
print("请输入各站到下一站的行驶时间：", end='')
t2 = list(map(int, input().split()))
t.extend(t2)
t.extend(t1)
M1 = int(input("M1: "))
M1a = list(map(int, input("请输入M1列车出发时间:").split()))
for i in range(M1):
    i1 = i
    for j in range(1, n+1):
        has_train[M1a[i]][j][0] = 1 # 在时刻a,车站j有向右的车
        M1a[i] = M1a[i] + t[j]  #加上到下一战的时间
M2 = int(input("M2: "))
M2a = list(map(int, input("请输入M2列车出发时间：").split()))
for i in range(M2):
    i1 = i
    for j in range(n, 0 ,-1):
        has_train[M2a[i]][j][1] = 1
        M2a[i] = M2a[i] + t[j-1]

#(3)由d[T][n] = 0这个位置来进行反推，T时刻最短等待时间为0，按照流程步骤实现3个决策，递归输出
for i in range(1,n):
    dp[T][i] =100
dp[T][n] = 0 # 在时刻T,车站n时不用等车
for i in range(T-1, -1, -1):
    for j in range(1, n+1, 1):
        dp[i][j] = dp[i+1][j] + 1 #原地不懂，等待一分钟
        if(j < n and has_train[i][j][0] > 0 and i + t[j] <= T): #搭乘往右边的车(如果右)
            dp[i][j] = min(dp[i][j], dp[i+t[j]][j+1])
        if(j>1 and has_train[i][j][1] > 0 and i+ t[j-1] <=T):   #搭乘往左边的车（如果有）
            dp[i][j] = min(dp[i][j], dp[i+t[j-1]][j-1])

if(dp[0][1] < 100):
    print("所需最少时间为",dp[0][1]) #最少等待时间会保存在dp[0][1]
else:
    print("不可能")


