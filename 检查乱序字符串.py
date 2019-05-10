#乱序字符串是指一个字符串只是另一个字符串的重新排列

#解法1：检查
def anagrmSolution1(s1, s2):
    alist = list(s2)
    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == s2[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None
            pos1 = pos1 + 1
        else:
            stillOK = False
    return stillOK and (len(list(filter(None, alist))) == 0)

print(anagrmSolution1('abc', 'acdb'))
#访问次数可以写成1到N整数的和，所以这个算法复杂度为O(n2)

#解法2：排序和比较
def anagrmSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(alist1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches

print(anagrmSolution2('qwer', 'xrewq'))
#线性迭代复杂度位O(n),排序通常是O(n^2)O(nlogn),所以排序操作比迭代花费更多

#解法3：穷举法
#找出排序的所有可能

#解法4：计数和比较
def anagrmSolution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    
    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False
    return stillOK

print(anagrmSolution4('dog', 'good'))
#前两个迭代都是n,第三个迭代有26步，T(n) = 2n + 26,  即O(n)
