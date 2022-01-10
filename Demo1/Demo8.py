#瑞年的判断
def Leap_Year(year) :
    if (year % 4)== 0:
        if(year%100 )== 0:
            if(year%400 )== 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


#调用函数，输出判断结果
year = int(input("请输入到判断的年份: "))
check_year = Leap_Year(year)
if check_year == True :
    print("{0}年是瑞年".format(year))
else:
    print("{0}年是平年".format(year))
