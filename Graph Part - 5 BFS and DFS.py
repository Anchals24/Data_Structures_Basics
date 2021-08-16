#Implementing Graph using Adjacency List Representation
""" 
Vertices : A , B , C , D , E 
Edges : (A -> B , A -> C , B -> A , B -> D , C -> A , C -> D , C -> E , D -> B , D -> C , D -> E , E -> C , E -> D) 

"""

#Step1 : Creating a list of all the vertices.
#Step2 : For each element (vertex) , we will create a list of its adjacent vertex.
#Let's implement using Python in built dictionary.
# Key will be the vertex and value will be its adjacent vertex. 

class Graph:
    def __init__(self , vertices):
        self.vertices = vertices
        self.adjlist = {}
        for vertex in self.vertices:
            self.adjlist[vertex] = []

    def display(self):
        for vertex in self.vertices:
            print(vertex , "->" , self.adjlist[vertex])

    def insert_edges(self , u , v):
        self.adjlist [u].append(v)
        self.adjlist [v].append(u) #{For undirected graphs}

    def degree(self , vertex):
        return len(self.adjlist[vertex])


vertices = ["A" , "B" , "C" , "D" , "E"]
all_edges = [("A", "B")  , ("A","C") , ("B" , "D") , ("C" , "D") , ("C" , "E") , ("D" , "E")]
G = Graph(vertices)
print("Initially the list looks like :")
G.display()
print("degree is : ", G.degree("D"))
#G.insert_edges("A" , "B")
#G.insert_edges("B" , "A")
for u , v in all_edges:
    G.insert_edges(u,v)
print("After inserting the edges: ")
G.display()
print("degree is : ", G.degree("D"))