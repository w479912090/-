'''
map ADT(abstract data type抽象数据类型)
Map() 创建一个新的空 map。
put(key，val) 向 map 中添加一个新的键值对。如果键已经在 map 中，那么用新值替换旧值。
get(key) 给定一个键，返回存储在 map 中的值，否则为 None。
del 使用 del map[key] 形式的语句从 map 中删除键值对。
len() 返回存储在映射中的键值对的数量。
in 返回 True 如果给定的键在 map 中。
'''

class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    #是否有左子树
    def hasLeftChild(self):
        return self.leftChild
    #是否有右子树
    def hasRightChild(self):
        return self.rightChild
    #是否是左子树
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    #是否是右子树
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    #是否是根
    def isRoot(self):
        return not self.parent
    #是否是叶子
    def isLeaf(self):
        return not (self.leftChild or self.rightChild)
    #是否有子节点
    def hasAnyChildren(self):
        return self.leftChild or self.rightChild
    #是否有两个子节点
    def hasBothChild(self):
        return self.leftChild and self.rightChild
    #替换节点数据
    def replaceNodeData(self, key, val, lc, rl):
        self.key = key
        self.payload = val
        self.leftChild = lc
        self.rightChild = rl
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.finMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
    def dinMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def __len__(self):
        return self.size
    def __setitem__(self, k, v):
        self.put(k, v)
    def put(self, key ,val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild(): 
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val)
    def __getitem__(self, key):
        return self.get(key)
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
    def __deleteitem__(self, key):
        self.delete(key)
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
    
    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.leftChild = None
        elif currentNode.hasBothChild():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.payload, currentNode.leftChild.leftChild, currentNode.rightChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload, currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)

myTree = BinarySearchTree()
myTree[3] = 'A'
myTree[1] = 'B'
myTree[2] = 'C'
myTree[4] = 'D'
myTree[5] = 'E'
print(myTree[1])
myTree.delete(1)
print(myTree[2])