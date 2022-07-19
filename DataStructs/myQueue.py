class myQueue:
    def __init__(self,size=10):         #创建构造函数，添加队列属性，默认队列大小为10
        self._content = []
        self._size = size
        self._current= 0

    def setsize(self,size):             #建立设置队列大小的方法
        if size < self._current:        #如果缩小队列，应删除后面的元素
            for i in range(size,self._current)[::-1]:
                del self._content[i]
            self._current = size

    def put(self,v):                    #创建入队的put（）方法，将元素插入到队列中
        if self._current < self._size:
            self._content.append(v)
            self._current = self._current + 1
        else:
            print('The Queue is full')

    def get(self):                      #创建出对的方法
        if self._content :
            self._current = self._current - 1
            return self._content.pop(0)
        else:
            print('The Queue is enmpty')

    def show(self):                     #创建显示队列当前元素的show（）方法
        if self._content:
            print(self._content)
        else:
            print('The Queue is empty')

    def empty(self):                    #创建清空队列所有元素的empty()方法
        self._content = []

    def isEmpty(self):                  #创建判断队列是否为空的方法
        if not self._content:
            return True
        else:
            return False

    def isFull(self):                   #创建判断队列是否已满的函数
        if self._current == self._size:
            return True
        else:
            return False

if __name__ == '__main__':
    q = myQueue()
    print('案例22：自定义队列')
    print('队列元素出队：')
    q.get()
    q.put(2)
    q.put(3)
    print('队列元素入队')
    q.show()
    print('队列是否已满：',str(q.isFull()))
    q.setsize(2)
    print('队列重设后是否已满：',str(q.isFull()))
    print('尝试添加新元素')
    q.put(3)
