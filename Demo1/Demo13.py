#乘法表的输出

for i in range(1,10) :
    for j in range(1,i+1) :
        s = i * j
        print("%d * %d = %d" % (i,j,s),end='，')

    print("\n")