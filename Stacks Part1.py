
#Implementation of a Stack using Lists 

class Stack:
    def __init__(self):
        self.elements = []

    def leng(self):
        return len(self.elements)
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def push(self,data):
        self.elements.append(data)
        print(self.elements)
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.elements.pop()

    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.elements[-1]
    
    
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