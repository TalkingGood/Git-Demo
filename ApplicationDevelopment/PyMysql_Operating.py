#coding=gbk
print("数据库的增删改查操作")
import pymysql

#（1） 创建数据库
def get_objetct():
    object = pymysql.connect(host='',port=3306,user='root',password='root',db='test1') #db表示数据库的名称
    return object

#（2） 连接数据库，插入一行完整数据
def insert(sql):
    object = get_objetct()
    cur = object.cursor()
    result = cur.execute(sql)
    print(result)
    object.commit()
    cur.close()
    object.close()
if __name__ == '__main__':
    sql = 'INSERT INTI test_student_table VALUES(1,\'zhang\', 12)' #插入信息的sql命令
    insert(sql) #调用名利给

#（3）插入多行数据
def insert_many(sql,args):
    objetct = get_objetct()
    cur = objetct.cursor()
    result = cur.executemany(query=sql,args=args)
    print(result)
    objetct.commit()
    cur.close()
    objetct.close()
if __name__ == '__main__':
    sql = 'INSERT INTO test_student_table VALUES (%s,%s,%s)'
    args = [(3,'li',11),(4,'sun',12),(5,'zhao',13)]
    insert_many(sql,args)

#(4)对数据库进行更改操作
def update(sql,args):
    object = get_objetct()
    cur = object.cursor()
    result = cur.execute(sql)
    print(result)
    object.commit()
    cur.close()
    object.close()
if __name__ == '__main__':
    sql = 'UPDATE test_student_table SET NAME= %s WHERE id = %s'
    args = ('zhang',1) #更改的信息内容
    update(sql,args)#调用命名

#（4）对更新后的数据库进行删除操作
def delete(sql,args):
    object = get_objetct()
    cur = object.cursor()
    result = cur.execute(sql,args)
    print(result)
    object.commit()
    cur.close()
    object.close()
if __name__ == '__main__':
    sql = 'DELETE FROM test_student_table WHERE id = %s;'

#(4)对数据库进行查询操作
def quary(sql, args):
    object = get_objetct()
    cur = object.cursor()
    cur.execute(sql,args)

    results = cur.fetchall()
    print(type(results)) #输出<class 'tuple'>,tuple元组类型
    for row in results:
        print(row)
        id = row[0]
        name = row[1]
        age = row[2]
        print('id: '+ str(id)+',  name:' + str(name)+ ', age:' + str(age))
    object.commit()
    cur.close()
    object.close()
if __name__ == '__main__':
    sql = 'SELECT * FROM test_student_table;' #返回<class 'tuple'>,tuple元组类型
    quary(sql,None) #调用查询语句进行查询
