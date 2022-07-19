def fun(elements, key, start, end):
    if elements[0] <= key <= elements[-1]:
        mid = (start + end) // 2  # // 表示取整形数
        if  elements[mid] == key :
            return mid
        if  start > end:
            return 'not found'
        elif elements[mid] < key:
            return fun(el, key, mid + 1, end)
        else:
            return fun(el, key, start, mid - 1)

    else:
        return 'not found'

print("折半查找案例")
print("请输入单调递增的整数数组")
el = [int(s) for s in input().split()]
print("请输入待查的数")
key = int(input())
end = len(el)
print("该数的下标是：")
print(fun(el, key, 0, end))


