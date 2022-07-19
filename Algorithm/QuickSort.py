
def QuickSock(List,low,high):
    #判断low是否小于high，如果不小于，直接返回元序列
    if low < high:
        i, j = low, high
        #设置基准数
        pivotkey = List[i]
        while i < j:
            # 如果列表后半区的数比基准大或相等， 则前移一位，直到有比基准小的数出现
            while i < j:
                #如果列表后半区的数比基准数大或相等， 则前移一位， 直到有比基准小的数出现
                j = j - 1
                #如找到， 放入前半区
                List[i] = List[j]
                #同样的方式比较前半区
                while (i < j) and (List[i] <= pivotkey):
                    i = i + 1
                    List[j] = List[i]
        #做完第一轮比较之后， 列表被分成了两个半区， 并且 i=j
        List[i] = pivotkey
        #递归前，后半区
        QuickSock(List, low, i -1)
        QuickSock(List, j + 1, high)
    return List

print("快递排序按咧")
List = [50, 10, 90, 30, 70, 40, 80, 60, 20]
print("排序前:", List)
QuickSock(List, 0, len(List) - 1)
print("排序后:", List)

