#裴波那契数列的实现


def fib(n) :
    if n == 1 :
        return [0]
    elif n == 2 :
        return [0,1]
    l = [0,1]
    for i in range(2,n) :
        l.append(l[-2]+l[-1])
    return l

num = int(input("please enter the number of items you want to output:"))
print(fib(num))




