#汉诺塔的实现（递归）

def move(n,a,b,c) :     #n为圆盘数，a代表第一根初始圆柱，b代表第二根圆柱，c代表第三根圆柱
    if n == 1 :
        print("从",a,"柱移动到",c,"柱")
    else:
        move(n-1,a,c,b) #将第一根圆柱的第n-1个圆盘移动到第二根过度圆盘
                        #此时上一级函数的第二根圆柱为目标圆柱
                        #第三根圆柱为过度圆柱，第一根为初始圆柱
        print("从",a,"柱移动到",c,"柱")
        move(n - 1, b, a,c)  # 将过度圆柱的第n-1个圆盘移动到目标圆柱
                             # 此时上一级函数的第二根圆柱为目标圆柱
                             # 第一根圆柱为过度圆柱，第三根为初始圆柱

D = int(input("请输入初始盘子数："))
E = input("请输入初始柱子名称：")
F = input("请输入初始柱子名称：")
G = input("请输入初始柱子名称：")
print("具体的移动过程如下：")
move(D,E,F,G)




