#顺序查找  复杂度是O(n)
def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(orderedSequentialSearch(testlist, 3))

#二分查找法  复杂度是O(logn)
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint+1:], item)

print(binarySearch(testlist, 8))

#Hash查找  时间复杂度平均为O(1)
'''
假设我们有整数项 54,26,93,17,77 和 31 的集合。我们的第一个 hash 函数，有时被称为 余数法 ，只需要一个项并将其除以表大小，返回剩余部分作为其散列值（h(item) = item％11）
负载因子，通常表示为 λ=项数/表大小
item            Hash Value
54                  10
26                  4
93                  5
17                  6
77                  0
31                  9

0       1       2       3       4       5       6       7       8       9       10
77     None   None    None     26      93      17      None    None    31       54
'''
#创建散列函数的几种方法
'''
1,分组求和法
电话号码 436-555-4601,分成2位数（43,65,55,46,01）,求和210，假设有11个槽，210%11=1，则电话号码散列到槽1
一些分组求和法会在求和之前每隔一个反转，43+56+55+64+01=209，209%11=10

2.平方取中法
先对该项平方，然后提取一部分数字结果  44*44=1936,取93，93%11=5，则44散列到槽5

3.基于字符的项（如字符串）创建哈希函数
比如cat字符串
ord('c') = 99   ord('a) = 97  ord('t) = 116     99+97+116 = 312     312%11 = 4
可以使用字符的位置作为权重
'''
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])*(pos+1)
    return sum%tablesize
print(hash('cat', 11))

#在冲突后寻找另一个槽的过程叫 重新散列  rehash(pos)=(pos + skip)％sizeoftable
#重要的是要注意，“跳过”的大小必须使得表中的所有槽最终都被访问

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key%size
    def rehash(self, oldhash, size):
        return (oldhash + 1)%size
    
    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        found = False
        stop = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.slots[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, item):
        self.put(key, item)

H = HashTable()
H[54] = 'cat'
H[77] = 'bird'
H[44] = 'goat'
print(H.slots)
print(H.data)


#冒泡排序   时间复杂度位O(n^2),稳定
def bubbleSort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
alist = [2,5,6,23,56,1,45,53,58,27]
bubbleSort(alist)
print(alist)

#短冒泡排序
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1
alist = [40,30,20,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)

#选择排序   时间复杂度是O(n^2)，不稳定，但是比冒泡排序的交还次数少
def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

#插入排序  时间复杂度是O(n^2)，稳定
def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue
alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

#希尔排序 时间复杂度是O(nlogn)~O(n^2),不稳定
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print('After increments is size', sublistcount, 'The list is', alist)
        sublistcount = sublistcount//2

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)

#归并排序 时间复杂度是O(nlogn),稳定
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

#快速排序 时间复杂度平均是O(nlogn),最差是O(n^2),不稳定
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)
def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)
def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
        print('快速排序', alist)
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

'''
总结
对于有序和无序列表，顺序搜索是 O(n)
在最坏的情况下，有序列表的二分查找是 O(logn)
哈希表可以提供恒定时间搜索。
冒泡排序，选择排序和插入排序是 O(n^2)
希尔排序通过排序增量子列表来改进插入排序。它落在 O(n)~O(n^2)之间
归并排序是 O(nlogn)，但是合并过程需要额外的空间。
快速排序是 O(nlogn)，但如果分割点不在列表中间附近，可能会降级到O(n^2)。它不需要额外的空间
'''