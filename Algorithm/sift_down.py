def sift_down(arr, node, end):
    root = node   #当前节点的位置
    while True:
        # 从root开始对最大堆调整
        child = 2 * root + 1 #左孩子的位置
        if child > end:
            break
        #找出两个中较大的一个
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            # 如果最大堆小于较大的孩子， 则交货顺序
            tmp = arr[root]
            arr[root] = arr[child]
            arr[child] = tmp
            root = child
        else:
            # 无须调整的时候， 退出
            break
def heap_sort(arr):
    # 从最后一个有字节点的孩子开始调整最大堆， 不断缩小调整的范围
    first = len(arr)  // 2 - 1
    for i in range(first, -1, -1):
        sift_down(arr, 1, len(arr) -1 )
    for end in range(len(arr) - 1, 0, -1):
        sift_down(arr, i, len(arr) - 1)
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)

def main():
    array = [16,9,21,13,4,11,3,22,8,7,15,27,8]
    print("堆排序案例")
    print("排序前：",array)
    heap_sort(array)
    print("排序后：",array)

if __name__ == '__main__':
    main()





