List = [9,5,3,15,9,7,2]
n = len(List)

#冒泡排序
for i in range(n-1):
    for j in range(n-1):
        if List[j] > List[j+1] :
            temp = List[j]
            List[j] = List[j+1]
            List[j+1] = temp

print("排序后：",List)

