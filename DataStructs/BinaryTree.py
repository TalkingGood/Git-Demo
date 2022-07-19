class Node:
    def __init__(self,item):
        self.item = item
        self.child1 = None
        self.child2 = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self,item):         #添加节点
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.child1 is None:
                    pop_node.child1 = node
                    return
                elif pop_node.child2 is None:
                    pop_node.child2 = node
                    return
                else:
                    q.append(pop_node.child1)
                    q.append(pop_node.child2)

    def preorder(self,root):        #前序遍历
        if root is None:
            return []
        result= [root.item]
        left_item =  self.preorder(root.child1)
        right_item = self.preorder(root.child2)
        return result + left_item + right_item

    def inorder(self, root):        #中序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder(root.child1)
        right_item = self.inorder(root.child2)
        return left_item + result + right_item

    def postorder(self,root):       #后序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.postorder(root.child1)
        right_item = self.postorder(root.child2)
        return left_item + right_item + result
    
if __name__ == '__main__':
    t = BinaryTree()
    for i in range(10):
        t.add(i)
    print('前序遍历：', t.preorder(t.root))
    print('中序遍历：', t.inorder(t.root))
    print('后序遍历：', t.postorder(t.root))






