#Implementing Queue using Lists:

class Queue:
    def __init__(self):
        self.elements = []
    
    def leng(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0
    
    def enqueue(self , data):
        self.elements.append(data)
        return self.elements
    
    def dequeue(self):
        if len(self.elements) == 0:
            return -1
        return self.elements.pop(0)

    def first(self):
        if len(self.elements) == 0:
            return -1
        return self.elements[0]

Q = Queue()
print(Q.is_empty())
print(Q.enqueue(4))
print(Q.enqueue(3))
print(Q.enqueue(1))
print(Q.dequeue())
print(Q.elements)
print(Q.leng())


            