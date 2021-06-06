"""

Implementation of stack using a linkedlist: 

Here we will be storing the data using a linked list 
and we will simply do it by creating nodes/tracking the address etc.
Let's start...

"""
#Step1 : Creating a Class Node using which we will create the Nodes of a Linkedlist.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Step2 : Create a class to implement Stack using Linked List....

class Stack_Linkedlist:
    def __init__(self):
        self.head = None

# Define a function to calculate the length of the stack. Complexity : O(n)

    def leng(self):
        temp = self.head
        cnt = 0
        while(temp):
            cnt += 1
            temp = temp.next
        return cnt

#Check whether the Stack is empty or not...........

    def is_empty(self):
        if self.head is None:
            return True 

#Push the elements into the Stack...............

    def push(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

#Pop the elements from the Stack................

    def pop(self):
        if self.head == None:
            return "stack is empty"
            
        tos = self.head
        self.head = self.head.next
        del(tos)

# Return the top most element of the Stack

    def top(self):
        if self.is_empty:
            print("stack is empty")
            return
        return self.head.data

#Print all the elements present in the Stack
    
    def traverse(self):
        temp = self.head
        while(temp):
            print(temp.data , end = " ")
            if temp.next is not None:
                print("->", end = " ")
            temp = temp.next

Stack = Stack_Linkedlist()
Stack.push(2)
Stack.push(5)
Stack.pop()
Stack.pop()
Stack.push(9)
Stack.push(3)
Stack.push(2)
Stack.push(1)
Stack.traverse()
 



