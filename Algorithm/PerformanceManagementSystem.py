# -*- coding: gbk -*-
def addStu(array):
    '''���ѧ����Ϣ'''
    stuDict = {}
    try:
        id = input("������ѧ��ѧ�ţ�")
        for i in range(len(array)):
            if array[i]['id'] == id:
                print("��ѧ����ѧ���Ѵ��ڣ������ظ����")
                return
        name = input("������ѧ�����֣�")
        age = input("������ѧ�����䣺")
        chinese = int(input("������ѧ�����ĳɼ���"))
        math = int(input("������ѧ����ѧ�ɼ���"))
        english = int(input("������ѧ��Ӣ��ɼ���"))
        stuDict['id'] = id
        stuDict['name'] = name
        stuDict['age'] = age
        stuDict['chinese'] = chinese
        stuDict['math'] = math
        stuDict['english'] = english
        stuDict['score'] = english + math + chinese
        array.append(stuDict) #�ѵ���ѧ����������ӵ��б���
        print("��ӳɹ�")
    except BaseException:
        print("�����쳣�����ʧ��")


#ɾ��ѧ����Ϣ
def delstu(array):
    try:
        id = input("������Ҫɾ��ѧ��ѧ�ţ�")
        for i in range(len(array)):
            if array[i]['id'] == id:
                del array[i]
                return 0
        return 1
    except BaseException:
        print("�����쳣��ɾ��ʧ��")
        return 2

#�޸�ѧ����Ϣ
def updateStu(array):
    try:
        id = input("������Ҫ�޸ĵ�ѧ��ѧ�ţ�")
        for i in range(len(array)):
            if array[i]['id'] == id:
                name = input("������Ҫ�޸ĵ�ѧ�����֣�")
                age = input("������Ҫ�޸ĵ�ѧ�����䣺")
                chinese = int(input("������Ҫ�޸ĵ�ѧ�����ĳɼ���"))
                math = int(input("������Ҫ�޸ĵ�ѧ����ѧ�ɼ���"))
                english = int(input("������Ҫ�޸ĵ�ѧ��Ӣ��ɼ���"))
                array[i]['name'] = name
                array[i]['age'] = age
                array[i]['chinese'] = chinese
                array[i]['math'] = math
                array[i]['english'] = english
                array[i]['score'] = english + math + chinese
                print("�޸ĳɹ�")
                return
        print("�Ҳ�����ѧ�ţ�û���޸� ")
    except BaseException:
        print("�����쳣���޸�ʧ��")

#��ѯѧ����Ϣ
def selectStu(array):
   try:
       id = input("������Ҫ��ѯѧ����ѧ�ţ�")
       for i in range(len(array)):
           if array[i]['id'] == id:
               print("��ѯ����ѧ����Ϣ��" , array[i])
       return
   except BaseException:
       print("�����쳣����ѯʧ��")
       return

print("�򵥵�ѧ���ɼ�����ϵͳ����")
print("**" * 30)
print("��ӭʹ��ѧ������ϵͳ")
print("1.���ѧ����Ϣ")
print("2.ɾ��ѧ����Ϣ")
print("3.�޸�ѧ����Ϣ")
print("4.��ѯѧ����Ϣ")
print("5.���ճɼ�����")
print("6.�˳�ϵͳ")
print("**" * 30)
flag = 0
array = []


#��flag��ǣ�ѡ��Ҫ���еĲ���������Ĳ�������Ϊ��������
while flag != 1:
    step = input("��������Ĳ�����")
    try:
        step = int(step)
    except BaseException:
        print("�����쳣����������Ĳ�����������")
        break
    if step == 1:
        addStu(array)
        print("ѧ����Ϣ��ӡ:",array)
    elif step == 2:
        num = delstu(array)
        if num == 0:
            print("ɾ���ɹ�")
        elif num == 1 or num == 3:
            print("ɾ��ʧ��")
        print("ѧ����ӡ��Ϣ", array)

    elif step == 3 :
        updateStu(array)
        print("ѧ����Ϣ��ӡ��",array)

    elif step == 4 :
        selectStu(array)
    elif step == 5:
        for i in range(len(array)):
            if array[i]['score'] < array[i-1]['score']:
                array[i], array[i-1] = array[i-1], array[i]

        print("ѧ����Ϣ�����", array)

    elif step == 6:
        flag = 1

    else:
        print("��������������������������")

print("�˳�ϵͳ�ɹ�")





