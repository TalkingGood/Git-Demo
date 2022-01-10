#导入数字计算的模块
import cmath
#输入相关数据

A = float(input('输入二次项系数A: '))
B = float(input('输入一次项系数B: '))
C = float(input('输入常熟C: '))

#利用求根公式计算结果
D = (B ** 2) - (4*A*C)
S1 = (-B - cmath.sqrt(D)) / (2*A)
S2 = (-B + cmath.sqrt(D)) / (2*A)

#输出计算结果
print(A,'x^2+',B,'x+',C,'=0 的结果为 {0} 和 {1}'.format(S1,S2))