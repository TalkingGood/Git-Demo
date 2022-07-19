import copy

class Matrix:
    def __init__(self,row,column,fill=0.0):
        self.shape =(row,column)
        self.row = row
        self.colum = column
        self._matrix = [[fill] * column for i in range(row)]

    def __getitem__(self, index):       #返回矩阵的行和列的元素的值
        if isinstance(index,int):
            return self._matrix[index-1]
        elif isinstance(index,tuple):
            return self._matrix[index[0]-1][index[1]-1]

    def __setitem__(self, index, value):        #设置矩阵的行和咧元素的值
        if isinstance(index,int):
            self._matrix[index-1] = copy.deepcopy(value)
        elif isinstance(index,tuple):
            self._matrix[index[0]-1][index[1]-1] = value

    def __eq__(self, N):            #比较唯独，也就是比较行数和列数
        '''相等'''
        assert isinstance(N,Matrix), "类型不匹配，不能比较"
        return N.shape == self.shape

    def __add__(self, N):           #将矩阵相加，矩阵能相加的条件是两个矩阵维度相等
        '''加法'''
        assert N.shape == self.shape,"维度不匹配，不能相加"
        M = Matrix(self.row,self.colum)
        for r in range(self.row):
            for c in range(self.colum):
                M[r,c] = self[r,c] + N[r][c]
        return M

    def show(self):                 #输出矩阵
        for r in range(self.row):
            for c in range(self.colum):
                print(self[r+1,c+1],end='  ')
            print()

if __name__ == '__main__':
    m = Matrix(3,3,fill=0.0)
    n = Matrix(3,3,fill=0.0)
    m[1] = [1.,2.,3.]
    m[2] = [4.,5.,6.]
    n[1] = [6.,8.,6.]
    n[2] = [1.,0.,3.]
    n[3] = [4.,9.,2.]
    p = m + n
    m.show()
    print() #空行
    p.show()
    print()
    print(p[1,1])


