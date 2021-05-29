#Example 1: I am trying to create a node and checking 
# how to print the address of a node or what can be an address of any node...

class Node: #created a Class Node 
    def __init__(self , data): #initializer #self parameter is mandatory to pass # we have only passed the data of a node.
        #we are dealing with only 1 part of the node which is data , 
        # initially we are considering that the next is empty. 
        #we are trying to create nodes and these are not linked.
    
        self.data = data  #(data of any node)
        self.next = None

newnode1 = Node(5) #newnode1 is an object 
#newnode1 is storing the address of the node()
#print(newnode1)
#print(newnode1.data)

#Example2 : I will try to create so many nodes and their next is still blank
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

newnode1 = Node(2)
newnode2 = Node(5)
newnode3 = Node(3)
newnode4 = Node(4)
#print(newnode1.data)
#print(newnode2.data)
#print(newnode3.data)
#print(newnode4.data)

#Example 3 : Let's try to link two nodes and create a basic linkedlist

class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

n1 = Node(3)
n2 = Node(6)
n3 = Node(7)
#print(n2)
n1.next = n2
n2.next = n3
#print(n1.data , end = "->")
#print(n1.next.data ,end = "->")
#print(n1.next.next.data)

class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
O = Linkedlist()
#print(O.head)