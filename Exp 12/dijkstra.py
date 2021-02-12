#1818123 Hariprasath S
inf = 9999
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        #[[0, 4, 4, 0, 0, 0], [4, 0, 2, 0, 0, 0], [4, 2, 0, 3, 1, 6], [0, 0, 3, 0, 0, 2], [0, 1, 0, 0, 0, 3], [0, 0, 6, 2, 3, 0]]

        for i in range(self.V):
            inner = []
            print("Enter distances from Node", i)
            for j in range(self.V):
                inner.append(int(input()))
            self.graph.append(inner)

        print(self.graph)

    def printSolution(self, dist, src, parent):
        print("\nSource Destination\tCost")
        for node in range(self.V):
            print(src, "   ->   ", node, "\t   ",dist[node])
        print(parent)

        for i in range(self.V):
            if i != src:
                print("Path = ", i, end="")
                j = i
                while j != src:
                    j = parent[j]
                    print(" <- ", j,end="")
            print("\n")


    def minDistance(self, dist, sptSet):
        min = inf

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        parent = [src] * self.V
        dist = [inf] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    parent[v] = u
        self.printSolution(dist,src,parent)

g = Graph(int(input("Enter the no of vertices: ")))
g.dijkstra(int(input("Enter the source node: ")))
