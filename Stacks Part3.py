"""
LifoQueue follows the LIFO Principle.  It is from the built-in module queue. 
The LifoQueue provides some handy methods that are useful in the stack implementation.
Such as : put(data) , get() , empty() , qsize()

#put(data) : push or add the data to the queue(in - built which we will use as a Stack only).
#get() : remove or pop the topmost element
#empty() : will check whether the stack is empty or not.
# qsize() : return the size of the stack/queue. 

# Let's begin now.................................................................................................

# Step1 : Firstly , Let us import Lifoqueue from the queue module!!!

"""

from queue import LifoQueue

# Let's create a Lifoqueue object...
Stack = LifoQueue()

# Let's check whether the stack is empty or not.....
print(Stack.empty())

#Now let's fill the stack by pushing the elements.
Stack.put(2)
Stack.put(4)
Stack.put(1)
Stack.put(9)

#Let's check whether the stack is empty or not...........
print(Stack.empty())

#Let's pop the few elements now....................
print(Stack.get())
print(Stack.get())

#Now let's check the stack size................
print("Size of the Stack =" , Stack.qsize())

#Let's pop all the elements now............
print(Stack.get())
print(Stack.get())

#Now let's check if the stack is empty..........
print(Stack.empty())
