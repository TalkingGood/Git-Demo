#coding=gbk
print("����������")

#��1������topsort()������ʵ���ز������������in_degrees������ʾ�����������ÿ���������ȣ�˧ѡ���Ϊ0�Ķ��㡣

def topsort(graph):
    in_degrees = dict((u,0) for u in graph) #��ʼ�����ж������Ϊ0
    vertex_num = len(in_degrees)
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1 #����ÿ����������
    Q = [ u for u in in_degrees if in_degrees[u] == 0 ] #ɸѡ���Ϊ0�Ķ���
    Seq = [] #�洢������

#��2��ɾ�����һ�����㲢�Ƴ���ָ�򣬶��ѭ�����ٴ�ɸѡ�����Ϊ0�Ķ���
    while Q:
        u = Q.pop() #Ĭ�ϴ����һ��ɾ��
        Seq.append(u)
        for v in graph[u]:
            in_degrees[v] -= 1 #�Ƴ�������ָ��
            if in_degrees[v] == 0:
                Q.append(v) #�ٴ�ɸѡ���Ϊ0�Ķ���
    if len(Seq) == vertex_num:   #���ѭ����������ڷ�0��ȵĶ��㣬˵��ͼ���л�����������������
        return Seq
    else:
        print("���ͼ���ڻ�")

#���������޻�ͼG,���ֵ����ʽ�洢��
G = {
    'a':'bf',
    'b':'cdf',
    'c':'d',
    'd':'ef',
    'e':'f',
    'f':''
}
print("������������", topsort(G))




