#阶乘的实现

j = 1
a = int(input("请输入需要的求的阶乘\n"))

for i in range(1,a+1) :
    j = j * i
print("结果为:",j)    