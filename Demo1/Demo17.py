#寻找最小公倍数

#定义寻找最小公倍数的函数
def Find(x,y) :
    #获取最大的数
    if x>y :
        max = x
    else :
        max = y
    while(True):
        if((max % x == 0) and (max % y == 0)):
            Find = max
            break
        max += 1
    return Find
#获取用户输入
num1 = int(input("请输入第一个数字： "))
num2 = int(input("请输入第二个数字： "))
print(num1,"和",num2,"的最小公倍数是：",Find(num1,num2))
