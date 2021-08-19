class Graph:
    def __init__(self , vertices):
        self.vertices = vertices
        self.adjlist = []
        for vertex in range(len(self.vertices)):
            self.adjlist.append([])
        
    def display(self):
        print(self.adjlist)
        for vertex in self.vertices:
            print(vertex , "->" , self.adjlist[vertex])    
    
    def insertedge(self , u , v):
        self.adjlist[u].append(v)
        

    def deleteedge(self , u , v):
        self.adjlist[u].remove(v)

    def degree(self , node):
        return len(self.adjlist[node])


Nodes = [0 , 1, 2, 3, 4 , 5]
G = Graph(Nodes)
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
print("After inserting --")
G.display()
print("Now, let's delete a few edges : ")
G.deleteedge(5 ,1)
G.display()

