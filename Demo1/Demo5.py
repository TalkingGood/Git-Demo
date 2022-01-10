# 随机整数
import random
x= random.randint(0,1000) #random.ranint(0,100)用于生成一个指定范围内的整数
print("生成随机整数：",x)

x= random.randrange(0,1000,2)#random.randrange(a,b,c)从指定范围内的集合中获取一个随机数
print("生成随机数：",x)

x= random.uniform(1,3) #random.uniform(a,b)用于生成指定范围内的随机浮点数
print("随机生成浮点数",x)