#coding=gbk
print("���ݿ����ɾ�Ĳ����")
import pymysql

#��1�� �������ݿ�
def get_objetct():
    object = pymysql.connect(host='',port=3306,user='root',password='root',db='test1') #db��ʾ���ݿ������
    return object

#��2�� �������ݿ⣬����һ����������
def insert(sql):
    object = get_objetct()
    cur = object.cursor()
    result = cur.execute(sql)
    print(result)
    object.commit()
    cur.close()
    object.close()
if __name__ == '__main__':
    sql = 'INSERT INTI test_student_table VALUES(1,\'zhang\', 12)' #������Ϣ��sql����
    insert(sql) #����������

#��3�������������
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

#(4)�����ݿ���и��Ĳ���
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
    args = ('zhang',1) #���ĵ���Ϣ����
    update(sql,args)#��������

#��4���Ը��º�����ݿ����ɾ������
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

#(4)�����ݿ���в�ѯ����
def quary(sql, args):
    object = get_objetct()
    cur = object.cursor()
    cur.execute(sql,args)

    results = cur.fetchall()
    print(type(results)) #���<class 'tuple'>,tupleԪ������
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
    sql = 'SELECT * FROM test_student_table;' #����<class 'tuple'>,tupleԪ������
    quary(sql,None) #���ò�ѯ�����в�ѯ
