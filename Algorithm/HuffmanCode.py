# coding=gbk
print("���������밸��")

#(1)����gengNode�࣬��ʼ����ֵ���Ӷ�����ڵ㡣����createNode()����������gengNode��
class gengNode():
    def __init__(self,freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq

    def isLeft(self):
        return self.father.left == self

def creteNode(freqs):
    return [ gengNode(freq) for freq in freqs]

#(2)������������huffmanTrees()����������Ҷ�ӽڵ㡣��������󣬽���Сֵ�Ӷ�����ȡ������ֵ����Ҷ�ӣ�������Сֵ�Ӷ�����ȡ������ֵ����Ҷ������ֵ�����Ϊ���ڵ㣬�ٽ����ֵ���������
def HuffmanTreess(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item:item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = gengNode(node_right.freq + node_left.freq)
        node_father.left = node_left
        node_left.father = node_father
        node_right.father= node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]

#(3)������������롣����Ҷ·������Ϊ0������Ҷ·������Ϊ1���ж��Ƿ�����forѭ����if������
def HuffmanEncodings(nodes, root):
    codes = ['']*len(nodes)
    for a in range(len(nodes)):
        node_tmp = nodes[a]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[a] = '0' + codes[a]
            else:
                codes[a] = '1' + codes[a]
            node_tmp = node_tmp.father
    return codes

if __name__ == '__main__':
    chars_freqs = [('C',2),('G',2),('E',2),('K',3),('B',4),('F',4),('I',4),('J',4),('D',5)
                   ,('H',6),('N',7),('M',9),('A',10)]
    nodes = creteNode([item[1] for item in chars_freqs])
    root = HuffmanTreess(nodes)
    codes = HuffmanEncodings(nodes,root)
    for item in zip(chars_freqs, codes):
        print('Character:%s free:%-2d  encoding:%s ' %(item[0][0],item[0][1],item[1]))
