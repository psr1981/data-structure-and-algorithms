class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = 0
        self.pred = None
        self.discoveryTime = 0
        self.finishTime = 0

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight


    def __str__(self):
        return (str(self.id) + ' connected To ' + str([ x.id for x in self.connectedTo]))

    def getConnections(self):
        return self.connectedTo.keys();

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPred(self, pred):
        self.pred = pred

    def getPred(self):
        return self.pred

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance

    def setDiscoveryTime(self, t):
        self.discoveryTime = t

    def getDiscoveryTime(self):
        return self.discoveryTime

    def setFinishTime(self, t):
        self.finishTime = t

    def getFinshTime(self):
        return self.finishTime

class Graph:
    
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices  + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

    def getVertices(self):
        return self.vertList.keys()

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], cost)


if __name__ == "__main__":

    g = Graph()
    for i in range(6):
        g.addVertex(i)

    g.vertList

    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))




