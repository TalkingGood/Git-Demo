# coding: gbk
print("收银员找钱案例---贪心算法")

#（1）存储每种硬币的面值，定义相关参数，用input（）函数得到每种零钱的数量
d = [0.01, 0.05, 0.1,0.5,1.0]  #存储每种硬币的面值
s = 0 #存储每种硬币的数量
d_num = [] #存储每种硬币的数量
temp = input('请输入每种零钱的数量：')
d_num0 = temp.split(" ")

#（2）用for循环计算出收银员共有多少零钱，得到需要找的零钱数额，判断当前找的零钱是否大于零钱总数。若是，则输出“零钱不够”，退出程序。
for i in range(0,len(d_num0)):
    d_num.append(int(d_num0[i]))
    s += d[i] * d_num[i] #计算出收银员共有多少零钱
sum = float(input("请输入需要找的零钱："))
if sum > s:
    #当输入的总金额比收银员的总金额多时，无法进行找零
    print("零钱不够")
    exit()

#（3）运用贪心算法----从面值大的钱币开始遍历，输出各面值硬币的数量
s = s - sum
result= {}
 #要想用的硬币数量最小，需要利用面值大的硬币，因此从面值大的硬币开始遍历
i = len(d) - 1
while i >= 0:
    if sum >= d[i]:
        n = int(sum / d[i])
        if n > d_num[i]:
            n = d_num[i] #更新n
        sum = sum - n * d[i] #贪心算法的关键步骤，改变sum的动态
        result[d[i]] = n
    i -= 1


if int(sum) > 0:
    print("零钱不够")
else:
    for a,b in result.items():
        print("用了%d个%f元硬币"%(b,a))




