#Implementing Queue using Lists:

#Create a class Queue.....
class Queue:
    #Initialize and create an empty list at the very beginning which will be used to store the queue data.
    def __init__(self):
        self.elements = []
    
    #Check the length of the queue.
    def leng(self):
        return len(self.elements)
    
    #Check whether the queue is empty or not...
    def is_empty(self):
        return len(self.elements) == 0
    
    #Inserting an element to the queue.....
    
    def enqueue(self , data):
        self.elements.append(data)
        return self.elements
    
    #Deleting an element from the queue....
    
    def dequeue(self):
        if len(self.elements) == 0:
            return -1
        return self.elements.pop(0)
    
    #Return the first element of the queue

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


            
