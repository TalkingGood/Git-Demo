def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i;
    return -1

print("线性查找案例")
# 在数组arr中查找字符D
arr = ['A', 'B', 'C' , 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'];
x = input("请输入你需要查找的元素：");
n = len(arr)
result = search(arr, n, x)
if(result == -1):
    print("元素不在数组中：")
else:
    print("元素在数组中的索引位置为", result)