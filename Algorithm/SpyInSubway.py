#coding=gbk
import numpy as np

print("������ļ������")
#��1������numpy������[i][j]��ʾʱ��i,�ڳ�վj���ٻ�Ҫ�ȴ��೤ʱ��
has_train = np.zeros((100,100,2))
dp = np.zeros((100,100)) #dp[i][j]��ʾʱ��i���ڳ�վj���ٻ�Ҫ�ȴ��೤ʱ��

#��2���������վ����n�����ʱ��T,��վ����һվ����ʻʱ��,M1,M1�г�����ʱ��,M2,M2�г�����ʱ���
n = int(input("���������վ����n:"))
T = int(input("��������ʱ��T:"))
t = [0]
t1 = [0] * (100 - n)
print("�������վ����һվ����ʻʱ�䣺", end='')
t2 = list(map(int, input().split()))
t.extend(t2)
t.extend(t1)
M1 = int(input("M1: "))
M1a = list(map(int, input("������M1�г�����ʱ��:").split()))
for i in range(M1):
    i1 = i
    for j in range(1, n+1):
        has_train[M1a[i]][j][0] = 1 # ��ʱ��a,��վj�����ҵĳ�
        M1a[i] = M1a[i] + t[j]  #���ϵ���һս��ʱ��
M2 = int(input("M2: "))
M2a = list(map(int, input("������M2�г�����ʱ�䣺").split()))
for i in range(M2):
    i1 = i
    for j in range(n, 0 ,-1):
        has_train[M2a[i]][j][1] = 1
        M2a[i] = M2a[i] + t[j-1]

#(3)��d[T][n] = 0���λ�������з��ƣ�Tʱ����̵ȴ�ʱ��Ϊ0���������̲���ʵ��3�����ߣ��ݹ����
for i in range(1,n):
    dp[T][i] =100
dp[T][n] = 0 # ��ʱ��T,��վnʱ���õȳ�
for i in range(T-1, -1, -1):
    for j in range(1, n+1, 1):
        dp[i][j] = dp[i+1][j] + 1 #ԭ�ز������ȴ�һ����
        if(j < n and has_train[i][j][0] > 0 and i + t[j] <= T): #������ұߵĳ�(�����)
            dp[i][j] = min(dp[i][j], dp[i+t[j]][j+1])
        if(j>1 and has_train[i][j][1] > 0 and i+ t[j-1] <=T):   #�������ߵĳ�������У�
            dp[i][j] = min(dp[i][j], dp[i+t[j-1]][j-1])

if(dp[0][1] < 100):
    print("��������ʱ��Ϊ",dp[0][1]) #���ٵȴ�ʱ��ᱣ����dp[0][1]
else:
    print("������")


