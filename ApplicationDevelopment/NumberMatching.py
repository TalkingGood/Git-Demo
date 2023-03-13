#coding=gbk
import re
#由用户输入需要匹配的数据
box = str(input('请输入数据：'))

#匹配字符串中的数字部分，并使其返回列表
num = re.findall('\w',box)
print(num)


