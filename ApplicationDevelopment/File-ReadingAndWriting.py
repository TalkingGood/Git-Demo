#coding=gbk
print("�ļ���д")

#��1�� txt�ļ�д��
f = open('text.txt','w',encoding='utf-8') #����Ϊ�ļ�·����û�и��ļ������´���
f.write('Python') #д������Ϊ�ַ���ģʽ
f.close() #���ùر��ļ��ĺ����������쳣����

 #txt�ļ���ȡ
f = open('text.txt','r')#��ȡʱ����ʹ�á�encoding=��,��ͬϵͳ��txt�����ʽ��һ����������޷���ȡ
data = f.readline() #.readlines()�����е����ݷ���һ���б��У�����read(()���������ݷ���һ���ַ�����
print(data)
f.close()

#(2)csv�ļ�д��
import csv #����csvģ��
rows = [['A','a'],['B','b'],['B','b']]
with open(r"test.csv",'w',newline='') as csv_file:
    # д��ʱ��Ҫ����newline = ''����
    wither = csv.writer(csv_file)
    for row in rows:
        wither.writerow(row)

#csv�ļ���ȡ
with open(r"test.csv",'r') as csv_file:
    reader = csv.reader(csv_file)
    print([row for row in reader])

#(3)xls�ļ���ȡд��
import xlwt
f = xlwt.Workbook(encoding= 'uft-8') # �����ʽΪ'utf-8'
sheet1 = f.add_sheet('test1') #����slx�ļ�sheet������
sheet2 = f.add_sheet('test2')
sheet1.write(0,0,'A') # write()��������ֵ�ֱ�Ϊ�У��У�д������
sheet1.write(0,1,'a')
sheet2.write(0,0,'B')
sheet2.write(1,0,'b')
f.save(r"excel.xls") #���洴����xls�ļ�
#xls�ļ���ȡ
import xlrd
filepath = r"excel.xls" #xls�ļ�·��
xls_file = xlrd.open_workbook(filepath) #��xls�ļ�
xls_sheet1 = xls_file.sheets()[0] # ��ȡ�ļ�sheet,sheet1��ӦֵΪ[0]
xls_sheet2 = xls_file.sheets()[1]
row = xls_sheet1.row_values(0) # ��ȡ��1����
col = xls_sheet2.col_values(0) # ��ȡ��2����
print(row)
print(col)


