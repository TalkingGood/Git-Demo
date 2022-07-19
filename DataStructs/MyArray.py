class MyArray:
    def __isNumber(self,n):
        if not isinstance(n,(int,float,complex)):
            return False
        return True

    def __init__(self,*args):  #argv的实质是将函数传入的参数，存储在元祖类型的变量args中。**kargs的实质
                               # 就是将函数的参数和值，存储在字典类型的变量kargs中
        if not args:
            self.value=[]
        else:
            for arg in args:
                if not self.__isNumber(arg):
                    print("All elements must be numbers")
                    return
            self.__value = list(args)

    def __add__(self, other):    #重载加法运算
        '''数组中每个元素都与数字other相加，或者两个数组相加，得到一个新的数组'''
        if self.__isNumber(other):
            #数组与数字相加
            b = MyArray()
            b.__value = [item + other for item in self.__value]
            return b
        elif isinstance(other,MyArray):
            #将两个数组对应的元素相加
            if(len(other.__value) == len(self.__value)):
                c = MyArray()
                c.__value = [i + j for i , j in zip(self.__value, other.__value)]
                #zip()函数用于将可迭代的对象作为参数，将对象中的元素打包乘元祖，然后返回由这些元素组成的列表
                return c
            else:
                print('Lenght no equal')
        else:
            print('Not supported')

    def dot(self,v):
        if not isinstance(v,MyArray):
            print('must be an instamce of MyArray')
            return

        if len(v) != len(self.__value):
            print('size must be equal.')
            return

        return sum([i*j for i,j in zip(self.__value,v.__value)])

    def __len__(self):
        return len(self.__value)

    def __str__(self):
        return str(self.__value)

    def __contains__(self, n):
        if n in self.__value:
            return True
        return False

    def append(self,n):
        if isinstance(n,(int,float)):
            self.__value.append(n)
        else:
            print('isinstance error')

    def __repr__(self):
        return repr(self.__value)

    def __getitem__(self, key):
        length = len(self.__value)
        if isinstance(key,int) and 0<= key <length :
            return self.__value[key]
        else:
            return 'Index Error'

    def __setitem__(self, key, value):
        length = len(self.__value)
        if isinstance(key,int) and 0<= key <length:
            self.__value[key] = value

        else:
            return 'Index Error'
if __name__ == '__main__':
    a = MyArray(1,2,3,4,5,6)
    b = MyArray(6,5,4,3,2,1)
    print('案例20：自定义数组的实现')
    print('数组a：',a)
    print('数组：', b)
    print('a+b:',a+b)
    print('a,b的内积：',a.dot(b))
    print('2是否在a内：',2 in a )
    a.append(7)
    print('a添加元素7：',a)
    print('查看a的第3个元素值：')
    print('查看a的第三个元素值：',a[2])
    a[6] = 0
    print('修改最后一项的值为0：',a)


