#分快查找

# (1) 常量数据定义块
Length = 9 #輸入數据的个数
flag = 0 #標記
pos = -1 #用于表示搜索元素在某快中的索引位置
tabNum = 3 #分快個數
tabPos = -1 #用于表示搜索元素在哪一快的索引
print("分快查找案例")
print("請輸入查找列表，以空格鍵避開數字：", end=' ')
list = [ int(s) for s in  input().split()]
goal = int(input("請輸入帶查找的數據： ")) # 用戶輸入帶查找數據
print("需要在列表中找到： ", goal)

# (2)使用二維列表表示多個子列表， 選擇序列前 tabNum 個元素排序后建立索引，根據索引建立子列表， 顯示構造的子列表
list_index = [] #使用二維列表表示多個子列表

# 在列表中添加列表
for i in range(tabNum):
    list_index.append([])

#會出現最大值在第二個子列表，第一子列表为空的情况
for i in range(1,tabNum):
    list_index[i].append(list[i -1])

#将添加元素的子列表中的元素降序排序--选择排序
for i in range(1, tabNum - 1):
    for j in range(1, tabNum -i):
        if list_index[j] < list_index[j + 1]:
            list_index[j] , list_index[j + 1] = list_index[j + 1]  , list_index[j]

#将其余元素添加到各个子列表，比索引大则放到，前一个子列表中，其余放入最后一个
for i in range( tabNum - 1, Length):
    for j in range(1, tabNum):
        if(list[i] > list_index[j][0]):
            list_index[j-1].append(list[i])
            break
    else:
        list_index[tabNum-1].append(list[i])

#提取第一个子列表的最大值作为索引
if len(list_index[0]) > 1:
    for i in range(len(list_index[0]) -1 , 0 , -1):
        if list_index[0][i] > list_index[0][i - 1]:
            list_index[0][i], list_index[0][i - 1] = list_index[0][i - 1], list_index[0][i]
print("子列表结构： ", list_index)


# (3) 将给定元素与各个子列表进行比较，确定给定元素位置，用flag标记元素是否找到，找到输出元素所在位置，否则输出“没有找到”
for i in range(tabNum, -1, -1):  #将给定元素与各个子列表进行比较，确定给定元素位置
    if len(list_index[i]) != 0 and goal < list_index[i][0]:
        for j in range(len(list_index[i])):
            if list_index[i][j] == goal:
                tabPos = i + 1
                pos = j + 1
                flag = 1

if flag:
    print("在第", tabPos, "个子列表中第", pos, "的位置")
else:
    print("没有找到")




print(list_index)

