class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__ (self):
        self.head = None
        
    def deep_copy(self):
        new_head = Node(self.head.data)
        temp1 = new_head
        temp = self.head.next
        while(temp):
            newnode = Node(temp.data)
            temp1.next = newnode
            temp = temp.next
            temp1 = temp1.next