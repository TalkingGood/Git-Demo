#coding=gbk
print("文件读写")

#（1） txt文件写入
f = open('text.txt','w',encoding='utf-8') #参数为文件路径，没有该文件则重新创建
f.write('Python') #写入内容为字符串模式
f.close() #调用关闭文件的函数，避免异常错误

 #txt文件读取
f = open('text.txt','r')#读取时不可使用‘encoding=’,不同系统的txt编码格式不一样，会造成无法读取
data = f.readline() #.readlines()将所有的数据放入一个列表中，而。read(()将所有数据放入一个字符串中
print(data)
f.close()

#(2)csv文件写入
import csv #引入csv模块
rows = [['A','a'],['B','b'],['B','b']]
with open(r"test.csv",'w',newline='') as csv_file:
    # 写入时需要加入newline = ''参数
    wither = csv.writer(csv_file)
    for row in rows:
        wither.writerow(row)

#csv文件读取
with open(r"test.csv",'r') as csv_file:
    reader = csv.reader(csv_file)
    print([row for row in reader])

#(3)xls文件读取写入
import xlwt
f = xlwt.Workbook(encoding= 'uft-8') # 编码格式为'utf-8'
sheet1 = f.add_sheet('test1') #创建slx文件sheet并命名
sheet2 = f.add_sheet('test2')
sheet1.write(0,0,'A') # write()函数三个值分别为行，列，写入内容
sheet1.write(0,1,'a')
sheet2.write(0,0,'B')
sheet2.write(1,0,'b')
f.save(r"excel.xls") #保存创建的xls文件
#xls文件读取
import xlrd
filepath = r"excel.xls" #xls文件路径
xls_file = xlrd.open_workbook(filepath) #打开xls文件
xls_sheet1 = xls_file.sheets()[0] # 读取文件sheet,sheet1对应值为[0]
xls_sheet2 = xls_file.sheets()[1]
row = xls_sheet1.row_values(0) # 读取表1的行
col = xls_sheet2.col_values(0) # 读取表2的列
print(row)
print(col)


