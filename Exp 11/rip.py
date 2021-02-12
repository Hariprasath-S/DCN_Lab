#1818123 Hariprasath S
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print("%d \t\t %d" % (i, dist[i]))

    def BellmanFord_algo(self, src):

        dist = [float("Inf")] * self.V
        dist[src] = 0

        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        self.printArr(dist)


v = int(input("Enter the no. of vertices:"))
e = int(input("Enter the no. of edges: "))
g = Graph(v)
for i in range(1, e + 1):
    a, b, c = eval(input(f"Enter source, destination and cost for edge {i}: "))
    g.addEdge(a, b, c)

g.BellmanFord_algo(0)