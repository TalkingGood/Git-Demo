class Stack:
    def __init__(self,size=10):             #创建构造函数，添加栈的属性
        self._content = []                  #使用列表存放栈的元素
        self._size = size                   #初始化栈的大小
        self._current = 0                   #栈中元素个数初始化为0

    def setSize(self,size):                 #建立设置栈大小的setSize()方法
        #如果缩小栈的空间，则删除已有元素
        if size < self._current:
            for i in range(size,self._current)[::-1]:
                del self._current[i]
            self._current = size
        self._size = size

    def push(self,v):                       #设置入栈push()方法
        if self._current < self._size:
            self._content.append(v)
            self._current = self._current + 1       #栈中元素个数加1
        else:
            print('Stack Full!')

    def pop(self):                          #设置出栈pop()方法
        if self._content:
            self._current = self._current - 1
            return self._content.pop()
        else:
            print('Stack is empty')

    def show(self):                         #设置显示当前元素的show()方法
        print(self._content)

    def empty(self):                        #设置清空栈的empty（）方法
        self._content = []
        self._current = 0

    def isEmpty(self):
        return not self._content

    def isFull(self):
        return self._current == self._size

if __name__ == '__main__':
    print('测试案例23：自定义栈的实现')
    s = Stack()
    print('测试栈是否为空：',str(s.isEmpty()))
    print('测试栈是否为满：',str(s.isFull()))
    s.push(1)
    s.push(2)
    s.push('a')
    print('添加元素后，显示栈当前元素：')
    s.show()
    s.setSize(3)
    print('设置栈的大小为3，继续添加元素：')
    s.push('b')
    print('弹出元素：',str(s.pop()))






