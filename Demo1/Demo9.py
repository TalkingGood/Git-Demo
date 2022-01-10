#获取最大数


#获取需要比较大小的数字
N = int(input("请输入需要对比大小的数字的个数: "))

#获取需要比较大小的数字
print("请输入需要对比的数字: ")
num = []
for i in range(1,N+1):
    temp = int(input("请输入第{0}个数字: ".format(i)))
    num.append(temp)


print("最大值为：",max(num))


