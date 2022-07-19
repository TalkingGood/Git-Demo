a = [5,6,3,32,56,7,1,31,32]
print("选择排序案例")
print("原数列：",a)

for i in range(len(a)):
    for j in range(len(a)):
        if a[j] > a[i]:
            a[i],a[j] = a[j],a[i]

print("排序之后的数列为：\n",a)