#coding=gbk
import re
#���û�������Ҫƥ�������
box = str(input('���������ݣ�'))

#ƥ���ַ����е����ֲ��֣���ʹ�䷵���б�
num = re.findall('\w',box)
print(num)


