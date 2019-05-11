class Stack():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
print(s.pop())
print(s.size())

#括号匹配
from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    index = 0
    stillOK = True
    while index < len(symbolString) and stillOK:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                stillOK = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    stillOK = False
        index = index + 1
    if stillOK and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

print(parChecker('((())))'))
print(parChecker('(((())))'))

print(parChecker('([{()})'))
print(parChecker('([{}])'))