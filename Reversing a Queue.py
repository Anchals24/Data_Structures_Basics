#Reversing a queue.....................................
from queue import Queue
from queue import LifoQueue

Q = Queue()
Stack = LifoQueue()

#print(Q.empty())
Q.put(3)
Q.put(2)
Q.put(1)
Q.put(5)
Q.put(4)
print(list(Q.queue))
L = Q.qsize()
while L != 0:
    deleted = Q.get()
    #print(deleted)
    Stack.put(deleted)
    L -= 1
print(Q.empty())
#print(Q.qsize())
#print(Stack.qsize())
L2 = Stack.qsize()
while L2 != 0:
    delete2 = Stack.get()
    print(delete2)
    Q.put(delete2)
    print(list(Q.queue))
    L2 -= 1
#print(Q.qsize())
#print(Stack.qsize())


        
        




























