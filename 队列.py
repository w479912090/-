class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        self.items.pop()
    def size(self):
        return len(self.items)

from pythonds.basic.queue import Queue

def hotPotato(nameList, num):
    simqueue = Queue()
    for name in nameList:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()

print(hotPotato(['a', 'b', 'c', 'd', 'e', 'f'], 7))

#双端队列Deque

class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

#从前面删除添加是O(1),从后面删除添加是O(n)

#回文检查
from pythonds.basic.deque import Deque

def palchecker(string):
    charDeque = Deque()

    for ch in string:
        charDeque.addRear(ch)
    stillOK = True

    while charDeque.size() > 1 and stillOK:
        if charDeque.removeFront() != charDeque.removeRear():
            stillOK = False
    return stillOK

print(palchecker('adcda'))