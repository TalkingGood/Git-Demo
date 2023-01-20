# -*- coding: gbk -*-
def addStu(array):
    '''添加学生信息'''
    stuDict = {}
    try:
        id = input("请输入学生学号：")
        for i in range(len(array)):
            if array[i]['id'] == id:
                print("该学生的学号已存在，不能重复添加")
                return
        name = input("请输入学生名字：")
        age = input("请输入学生年龄：")
        chinese = int(input("请输入学生语文成绩："))
        math = int(input("请输入学生数学成绩："))
        english = int(input("请输入学生英语成绩："))
        stuDict['id'] = id
        stuDict['name'] = name
        stuDict['age'] = age
        stuDict['chinese'] = chinese
        stuDict['math'] = math
        stuDict['english'] = english
        stuDict['score'] = english + math + chinese
        array.append(stuDict) #把单个学生的数据添加到列表中
        print("添加成功")
    except BaseException:
        print("发生异常，添加失败")


#删除学生信息
def delstu(array):
    try:
        id = input("请输入要删除学生学号：")
        for i in range(len(array)):
            if array[i]['id'] == id:
                del array[i]
                return 0
        return 1
    except BaseException:
        print("发生异常，删除失败")
        return 2

#修改学生信息
def updateStu(array):
    try:
        id = input("请输入要修改的学生学号：")
        for i in range(len(array)):
            if array[i]['id'] == id:
                name = input("请输入要修改的学生名字：")
                age = input("请输入要修改的学生年龄：")
                chinese = int(input("请输入要修改的学生语文成绩："))
                math = int(input("请输入要修改的学生数学成绩："))
                english = int(input("请输入要修改的学生英语成绩："))
                array[i]['name'] = name
                array[i]['age'] = age
                array[i]['chinese'] = chinese
                array[i]['math'] = math
                array[i]['english'] = english
                array[i]['score'] = english + math + chinese
                print("修改成功")
                return
        print("找不到该学号，没法修改 ")
    except BaseException:
        print("发生异常，修改失败")

#查询学生信息
def selectStu(array):
   try:
       id = input("请输入要查询学生的学号：")
       for i in range(len(array)):
           if array[i]['id'] == id:
               print("查询到的学生信息：" , array[i])
       return
   except BaseException:
       print("发生异常，查询失败")
       return

print("简单的学生成绩管理系统案例")
print("**" * 30)
print("欢迎使用学生管理系统")
print("1.添加学生信息")
print("2.删除学生信息")
print("3.修改学生信息")
print("4.查询学生信息")
print("5.按照成绩排序")
print("6.退出系统")
print("**" * 30)
flag = 0
array = []


#用flag标记，选择要进行的操作，输入的操作代号为数字类型
while flag != 1:
    step = input("请输入你的操作：")
    try:
        step = int(step)
    except BaseException:
        print("输入异常，可能输入的不是数字类型")
        break
    if step == 1:
        addStu(array)
        print("学生信息打印:",array)
    elif step == 2:
        num = delstu(array)
        if num == 0:
            print("删除成功")
        elif num == 1 or num == 3:
            print("删除失败")
        print("学生打印信息", array)

    elif step == 3 :
        updateStu(array)
        print("学生信息打印：",array)

    elif step == 4 :
        selectStu(array)
    elif step == 5:
        for i in range(len(array)):
            if array[i]['score'] < array[i-1]['score']:
                array[i], array[i-1] = array[i-1], array[i]

        print("学生信息排序后：", array)

    elif step == 6:
        flag = 1

    else:
        print("操作类型输入有误，请重新输入")

print("退出系统成功")





