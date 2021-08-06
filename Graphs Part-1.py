"""GRAPH ADT {in general} """

import numpy as np

class Graph:
    def __init__(self , vertices):
        self.vertices = vertices 
        #Let's create the adjacency matrix.
        self.adjmat = np.zeros((vertices , vertices)) #np.zeros is a function which will assign 0 to all the cells. 
        #(vertices , vertices ) : Is a tuple. which means number of rows n columns want in the matrix.
    
    def insert_edge(self , u , v , w = 1): 
        #To insert an edge , )'ll take 4 parameters. 
        #self , u : vertex , v : vertex , w : weight/cost 
        # (by default we'll take it as 1 so that we can later on use it in unweighted graphs as well.)
        self.adjmat[u][v] = w
    
    def remove_edge(self , u , v):
        self.adjmat[u][v] = 0

    def edge_exist(self , u , v):
        return self.adjmat[u][v] == 1

    def vertex_count(self):
        return self.vertices

    def edge_count(self):
        count = 0
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjmat[i][j] == 1:
                    count += 1
        return count

    def vertices(self): #doubt #returns the set of vertices.
        for i in range(self.vertices):
            print(i , end = "")
        print()

    def edges(self): #returns the set of edges.
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjmat[i][j] != 0:
                    print(i , "--" , j)

    def outdegree(self , v): #traverse columns of that particular vertex.
        count = 0
        for j in range(self.vertices):
            if self.adjmat[v][j] != 0:
                count += 1
        return count

    def indegree(self , v) : #traverse rows of that particular vertex.
        count = 0
        for i in range(self.vertices):
            if self.adjmat[v][i] != 0:
                count += 1
        return count

    def display_adjmat(self): #not a part of ADT but it will help us to visualize our matrix
        print(self.adjmat)
