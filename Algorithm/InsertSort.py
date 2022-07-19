
def InsertSort(myList):
    length = len(myList)
    for i in range(1,length):
        j = i-1
        if (myList[i] < myList[j]):
            temp = myList[i]
            myList[i] = myList[j]
            j  = j - 1
            while j >=0 and myList[j] > temp:
                myList[j+1] = myList[j]
                j = j - 1
            myList[j + 1 ] = temp

if __name__ == '__main__':
    print("插入排序案例：")
    myList = [49,38,65,97,76,13,27,49]
    print("排序前：",myList)
    InsertSort(myList)
    print("排序后：",myList)






