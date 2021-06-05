#Implementation of a Stack using Lists 

#In this , I have simply implemented stacks using lists...
#Step1 : Let's define a class stack....

class Stack:
    def __init__(self):
        #Let's initialize an empty list....... We will use list to store the data here.
        self.elements = []

    def leng(self):
        #Similar to lists : "len()" has been used to determine the length of the list.
        return len(self.elements)
    
    #Function to check whether the stack is empty or not.
    def is_empty(self):
        return len(self.elements) == 0
    
    #Function to insert the data into the stack...
    def push(self,data):
        self.elements.append(data)
        print(self.elements)
    
    #Function to delete data from the stack....
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.elements.pop()
    
    #Function to find out the top element of the stack.......
    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.elements[-1] #similar to find the last element of the list using negative indexing.
    
    
stack = Stack()
print(stack.is_empty())
stack.push(2)
stack.push(1)
stack.push(4)
stack.push(3)
print(stack.leng())
print(stack.is_empty())
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.elements)
stack.push(5)
stack.push(3)
stack.push(1)
stack.push(0)
print(stack.pop())
print(stack.top())

#Time Complexity : O(1)  
