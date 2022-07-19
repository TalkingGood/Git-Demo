class DirecteGraph(object):
    def __init__(self,d):               #__init__()方法，储存输入的数据
        if isinstance(d,dict):
            self.__graph = d
        else:
            self.__graph = dict()
            print('Str error')

    def __generatePath(self,graph,path,end,results):
        curret = path[-1]
        if curret == end:
            results.append(path)
        else:
            for n in graph[curret]:
                if n not in path:
                    self.__generatePath(graph,path + [n],end,results)

    def searchPath(self,start,end):
        self.__results = []
        self.__generatePath(self, graph, [start], end,self, results)
        self.__results.sort(key=lambda x:len(x))        #按所有长度进行排序
        print('The path from ',self,results[0][0],'to',self.__results[0][-1]'is:')
        for path in self.__results:
            print(path)