class Student:
    def __init__(self,name,score):              #初始化各个形参
        self.name = name
        self.score = score

    def __hash__(self):                         #使用哈希算法把形参转为一个数值
        return self.name.__hash__()

    def __eq__(self, other):                    #把转换过来的数值进行比较
        if self.score == other.score:
            return True
        return False

    def __repr__(self):                         #实现自我描述的功能
        return self.name + ';' + self.score


if __name__ == '__main__':
    u1 = Student('Lisa', '99')
    u2 = Student('Bart', '59')
    u3 = Student('Anna', '66')
    u4 = Student('Jerry', '69')
    u5 = Student('Roy', '86')
    u6 = Student('Karry', '86')
    a = {u1, u2, u3, u4}
    b = {u4, u5, u6}

    #创建u,s两个集合
    u = set(a)
    s = set(b)
    print("原来的集合u为", u)
    print("原来的集合s为", s)

    #进行增添，删除操作
    u.remove(u2)
    s.add(u2)
    print("删除后的集合u为", u)
    print("删除后的集合s为", s)

    #进行集合的运算并输出
    print("集合u与集合s的并集为", u|s)
    print("集合u与集合s的交集为", u&s)
    print("集和u与集合s的差集为", u-s)

