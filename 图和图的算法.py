#Vertex:图中的每个顶点
class Vertex:
    def __init__(self, key):
        self.id = key
        #每个顶点使用字典来跟踪它连接的顶点和每个边的权重
        self.connectedTo = {}
    #从这个顶点添加一个连接到另一个
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    def __str__(self):
        return str(self.id) + 'connectedTo:' + str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

#Graph:保存顶点的主列表
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
    def __contains__(self, key):
        return key in self.vertList
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())

g = Graph()
for i in range(6):
    g.addVertex(i)
g.addEdge(0, 1, '01')
g.addEdge(1, 2, '12')
g.addEdge(2, 3, '23')
g.addEdge(3, 4, '34')
g.addEdge(4, 5, '45')
g.addEdge(5, 0, '50')
for v in g:
    for w in v.getConnections():
        print('(%s, %s, %s)' % (v.getId(), w.getId(), v.getWeight(w)))

#构建字梯图
from pythonds.graphs import Graph

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = word
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1!=word2:
                    g.addEdge(word1, word2)
    return g

g = buildGraph('zititu.txt')