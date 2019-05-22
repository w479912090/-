'''
基本操作
BinaryHeap() 创建一个新的，空的二叉堆。
insert(k) 向堆添加一个新项。
findMin() 返回具有最小键值的项，并将项留在堆中。
delMin() 返回具有最小键值的项，从堆中删除该项。
如果堆是空的，isEmpty() 返回 true，否则返回 false。
size() 返回堆中的项数。
buildHeap(list) 从键列表构建一个新的堆。
'''

from pythonds.trees.binheap import BinHeap

bh = BinHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
print(bh.delMin())
print(bh.heapList)

class BinHeap1:
    def __init__(self):
        self.headList = [0]
        self.currentSize = 0
    #新添加的项小于其父项，将项与其父项交换, 当前节点的父节点可以通过将当前节点的索引除以2来计算
    def percUp(self, i):
        while i//2>0:
            if self.headList[i] < self.headList[i//2]:
                tmp = self.headList[i//2]
                self.headList[i//2] = self.headList[i]
                self.headList[i] = tmp
            i = i//2
    #添加一个新项
    def insert(self, k):
        self.headList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(k)
    #删除最小项,也就是根项
    def delMin(self):
        retval = self.headList[1]
        self.headList[1] = self.headList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.headList.pop()
        self.percDown(1)
        return retval
    #获取列表中的最后一个项并将其移动到根位置来恢复根项,将根节点和最小的子节点交换
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.headList[i] > self.headList[mc]:
                tmp = self.headList[i]
                self.headList[i] = self.headList[mc]
                self.headList[mc] = tmp
            i = mc
    #获取最小项
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.headList[i*2] < self.headList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    #从一个列表构建一个堆
    def buildHeap(self, alist):
        i = len(alist)//2
        self.currentSize = len(alist)
        self.headList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i = i - 1

newBh = BinHeap1()
newBh.buildHeap([9, 5, 6, 2, 3])
print(newBh.headList)

# O(n) 时间构建堆    使用堆对列表在 O(nlogn) 时间内排序
