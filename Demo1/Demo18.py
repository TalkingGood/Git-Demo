#计算器的实现

#获取用户输入带计算的数字
#首先选择运算的技能
print("选择运算：")
print("1.想加")
print("2.相减")
print("3.相乘")
print("4.相除")
choice = input("请输入你的选择（1/2/3/4）: ")
#然后获取需要运算的数字
num1 = int(input("输入第一个数字："))
num2 = int(input("输入第二个数字："))

#定义具有相加功能的函数
def add(x,y) :
    '''相加'''
    return x+y
#定义具有相减功能的函数
def subtract(x,y) :
    '''相减'''
    return x-y
#定义具有相乘功能的函数
def multiply(x,y) :
    '''相乘'''
    return x*y
#定义具有相除功能的函数
def divide(x,y) :
    '''相除'''
    return x/y

def show(choice,num1,num2) :
    if choice == '1' :
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice == '2' :
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif choice == '3' :
        print(num1,"*",num2,"=",multiply(num1,num2))
    elif choice == '4' :
        print(num1,"/",num2,"=",divide(num1,num2))
    else :
        print("非法输入")

#展示输出
show(choice,num1,num2)
