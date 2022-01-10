#寻窄最大公约数

#定义寻找最大公约数的函数
def Find(x,y) :
    #获取最小值
    if x > y :
        min = y
    else :
        min = x
    for i in range(1,min+1) :
        if((x%i==0)and (y%i==0)):
            Find = i
    return Find

#用户输入数据
num1 = int(input("请输入第一个数字: "))
num2 = int(input("请输入第二个数字: "))
print(num1,"和",num2,"的最大公约数为：",Find(num1,num2))



