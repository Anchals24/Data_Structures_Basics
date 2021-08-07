from collections import deque
class Graph2:
    def __init__(self , vertices):
        self.vertices = vertices
        #let's create the matrix without using numpy
        self.adjmat = []
        for v in range(vertices):
            columns = [0] * vertices
            self.adjmat.append(columns)

    def insert_edge(self , u , v , w = 1): 
        #To insert an edge , )'ll take 4 parameters. 
        #self , u : vertex , v : vertex , w : weight/cost 
        # (by default we'll take it as 1 so that we can later on use it in unweighted graphs as well.)
        self.adjmat[u][v] = w
    
    def remove_edge(self , u , v):
        self.adjmat[u][v] = 0
        
    def display_adjmat(self): #not a part of ADT but it will help us to visualize our matrix
        print(self.adjmat)
        #print()

    #BFS :
    """ 
        - BFS : Breadth First Search.
        - Similar to Level Order Traversal.
        - Will be traversing level wise.
        - BFS starts from a vertex "s".
        - Then , will find the adjacent vertex of "s" , insert them into the queue and traverse them level wise.
        - Vertex which has already been visited won't be considered again.
        - loop will end when the queue will not be having any vertex.
        
    """
    def BFS(self , s):
        i = s
        self.q = deque() #importing queue
        visited = [0] * self.vertices #creating a list of len ( total number of vertices) and initialize to 0.
        print(i , end =" ")
        visited[i] = 1
        self.q.append(i)
        while self.q:
            i = self.q.popleft()
            for j in range(self.vertices):
                if self.adjmat[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    print(j , end= " ")
                    self.q.append(j)

    def helperdfs(self , s , visited):
        if visited[s] == 0:
            print(s , end = " ")
            visited[s] = 1
        for j in range(self.vertices):
            if self.adjmat[s][j] == 1 and visited[j] == 0:
                self.helperdfs(j , visited)


    #DFS:
    """
    - Depth First Search starts at a vertex.
    - Select the adjacent vertex from the start vertex.
    - Visit the adjacent vertex , mark as visited.
    - Continue the above procedure until there are no more unexplored edges.
    - then terminate.
    """
    def DFS(self ,s):
        visited = [0] * self.vertices
        self.helperdfs(s , visited)
        

G = Graph2(7)
#G.display_adjmat()
#print("Vertices:" , G.vertex_count())
#print("Edges:" , G.edge_count())
G.insert_edge(0 ,1)
G.insert_edge(0 ,5)
G.insert_edge(0 ,6)
G.insert_edge(1 ,0)
G.insert_edge(1 ,2)
G.insert_edge(1 ,5)
G.insert_edge(2 ,3)
G.insert_edge(2 ,4)
G.insert_edge(2 ,6)
G.insert_edge(3 ,4)
G.insert_edge(4 ,2)
G.insert_edge(4 ,5)
G.insert_edge(5 ,2)
G.insert_edge(5 ,3)
G.insert_edge(6 ,3)
G.display_adjmat()
print("BFS: ") , G.BFS(0)
print()
print("DFS: ") , G.DFS(0)