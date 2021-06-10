""" Implementing Queue using Linked list """

class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.head = None

    #Check the length of the queue.................

    def __len__(self):
        cnt = 0
        temp = self.head
        while(temp):
            cnt += 1
            temp = temp.next
        return cnt

    #check whether the queue is empty or not...........

    def __isempty__(self):
        return self.head == None

    #inserting an element to the queue.........

    def __enqueue__(self , data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = newnode

    # deleting an element from the queue......

    def __dequeue__(self):
        if self.head == None:
            return -1
        else:
            temp = self.head
            self.head = temp.next
            del(temp)

    #return the first element..
    def __first__(self):
        if self.head == None:
            return -1
        else:
            return self.head.data

    #Print all the elements of the queue

    def traverse(self):
        temp = self.head
        while(temp):
            print(temp.data , end = " ")
            if temp.next is not None:
                print("->", end = " ")
            temp = temp.next

Q = QueueLinkedList()
print(Q.__len__())
Q.__enqueue__(4)
Q.__enqueue__(8)
Q.__enqueue__(3)
Q.__enqueue__(2)
Q.traverse()

Q.__dequeue__()
print(Q.__len__())
Q.traverse()








