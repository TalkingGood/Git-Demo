#coding=gbk
print("给任务排序")

#（1）定义topsort()函数，实现拓步任务的排序。用in_degrees参数表示入度数。计算每个顶点的入度，帅选入度为0的顶点。

def topsort(graph):
    in_degrees = dict((u,0) for u in graph) #初始化所有顶点入度为0
    vertex_num = len(in_degrees)
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1 #计算每个顶点的入度
    Q = [ u for u in in_degrees if in_degrees[u] == 0 ] #筛选入读为0的顶点
    Seq = [] #存储排序结果

#（2）删除最后一个顶点并移除其指向，多次循环，再次筛选入读度为0的顶点
    while Q:
        u = Q.pop() #默认从最后一个删除
        Seq.append(u)
        for v in graph[u]:
            in_degrees[v] -= 1 #移除其所有指向
            if in_degrees[v] == 0:
                Q.append(v) #再次筛选入度为0的顶点
    if len(Seq) == vertex_num:   #如果循环结束后存在非0入度的顶点，说明图中有环，不尊在拓扑排序
        return Seq
    else:
        print("这个图存在环")

#定义有向无环图G,用字典的形式存储。
G = {
    'a':'bf',
    'b':'cdf',
    'c':'d',
    'd':'ef',
    'e':'f',
    'f':''
}
print("任务排序结果：", topsort(G))




