#质数的判断

#输入
num1 = int(input("请输入等待判断的第一个数字: "))
num2 = int(input("请输入等待判断的第二个数字: "))

#编写比较数字的函数
def Prime_Number(num):
    if num > 2 :
        for i in range(2,num):
            if (num % i) == 0 :
                print(num,"不是质数")
                print(i,"乘以",num//i,"是",num)
                break

            for j in range(2,num):
                if(num % j) != 0 :
                    print(num,"不是质数")
                    print(j,"乘以",num//j,"是",num)
                    break
                    
    else:
        print(num,"是质数")

#调用函数并且输出比较结果
Prime_Number(num1)
Prime_Number(num2)




