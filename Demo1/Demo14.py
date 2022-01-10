#阿姆斯特浪数的实现

#判断是否为阿姆斯特朗数
num = int(input("请输入一个数: "))
sum = 0
n = len(str(num))
temp = num

#建立一个while循环
while temp > 0 :
    digit = temp % 10
    sum += digit ** n
    temp //= 10

#通过if来判断
if sum == num :
    print(num,"是阿姆斯特朗数")
else :
    print(num,"不是阿姆斯特朗数")


#输出范围内阿姆斯特朗数
max = int(input("请输入最大值: "))
min = int(input("请输入最小值: "))
#建立for循环
for num in range(min,max) :
    sum = 0
    n = len(str(num))
    temp = num
    while temp > 0 :
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    if sum == num :
        print(num)



