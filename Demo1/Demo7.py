#收到待判断的奇偶数的数字、
num = int(input("请输入待判断的奇偶数的数字: "))

#判断并且输出判断的结果
if (num%2 ) ==0 :
    print("{0}是偶数".format(num))
else:
    print("{0}是奇数".format(num))
