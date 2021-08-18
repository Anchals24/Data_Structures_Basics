from collections import deque
class Graph:
    def __init__(self , vertices):
        self.vertices = vertices
        self.adjlist = {}
        for vertex in self.vertices:
            self.adjlist[vertex] = []
    
    def display(self):
        for vertex in self.vertices:
            print(vertex, "->" , self.adjlist[vertex])
    
    def insertedge(self , u , v ):
        self.adjlist[u].append((v))

    def deleteedge(self , u , v):
        self.adjlist[u].remove(v)
    
    def degree(self , vertex):
        return len(self.adjlist[vertex])

    def BFS(self , s):
        i = s
        self.q = deque()
        visited = [0] * len(self.vertices)
        print(i , end = " ")
        visited[i] = 1
        self.q.append(i)
        while self.q:
            i = self.q.popleft()
            for j in self.adjlist[i]:
                if visited[j] == 0:
                    visited[j] = 1
                    print(j , end = " ")
                    self.q.append(j)

    def helperdfs(self , s , visited):
        if visited[s] == 0:
            print(s , end = " ")
            visited[s] = 1
        for j in self.adjlist[s]:
            if visited[j] == 0:
                self.helperdfs(j , visited)

    def DFS(self , s):
        visited = [0] * len(self.vertices)
        self.helperdfs(s , visited)


nodes = [0, 1 , 2, 3, 4, 5]
G = Graph(nodes)
print("Before inserting anything --")
G.display()
G.insertedge(1 , 3 )
G.insertedge(1 , 2 )
G.insertedge(2 , 4 )
G.insertedge(3 , 1 )
G.insertedge(3 , 5)
G.insertedge(4 , 3)
G.insertedge(4 , 5)
G.insertedge(5 , 1)
print("After inserting all the edges --")
G.display()
#G.deleteedge(3 , 5)
#print("After removing an edge --")
#G.display()
print("BFS is :  ")
G.BFS(2)
print()
print("DFS is : ")
G.DFS(1)
