class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__ (self):
        self.head = None

# Function 1 : Insert a new node at the beginning:

    def _insert_at_beginning_(self , data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    
        
#Function 2 : Insert a new node at the end:

    def insert_at_end (self , data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = newnode

        #print each node data of a linkedlist:

    def delete_the_first_node(self ):
        
        temp = self.head
        #print(self.head)
        self.head = self.head.next
        del(temp)

    def delete_the_last_node(self):
        #print("12")
        temp = self.head
        #print("temp.data" , temp.data)
        while(temp.next):
            ls = temp
            temp = temp.next
            #print("updated temp" , temp)
            #print(temp.data)
            Lss = ls.next
            if Lss.next is None:
                ls.next = None
        #print(temp.data) 
        #print(temp)
        del(temp)
    
    def insert_at_middle(self , data , pos):
        newnode1 = Node(data)
        temp = self.head
        pos_temp = 1
        while(temp.next):
            middle = temp
            temp = temp.next
            if (pos - pos_temp == 1):   
                middle.next = newnode1
                newnode1.next = temp
                pos_temp += 1
            else:
                pos_temp += 1

    def delete_from_middle(self , pos):
        temp = self.head
        pos_t = 1
        while(temp.next):
            middle = temp
            temp = temp.next
            tbd = temp
            if (pos_t + 1 == pos):
                middle.next = temp.next
                del(tbd)
                pos_t += 1
            else:
                pos_t += 1

    def searching_list(self , data):
        temp = self.head
        Flag = True
        while (temp.next):
            if temp.data == data :
                print(temp)
                Flag = False
                break
            temp = temp.next
        if Flag == True:
            print(-1)

    def traverse_the_list(self):
        temp = self.head
        while(temp):
            print(temp.data , end = " ")
 
            if temp.next is not None:
                print('->' , end = " ")
            temp = temp.next

l1 = Linkedlist()
l1._insert_at_beginning_(2)
l1._insert_at_beginning_(3)
l1._insert_at_beginning_(4)
l1._insert_at_beginning_(7)
l1._insert_at_beginning_(2)
l1._insert_at_beginning_(10)
l1._insert_at_beginning_(9)
#l1.insert_at_end(2)
#l1.insert_at_end(3)
#l1.delete_the_first_node()
#l1.delete_the_last_node()
#l1.searching_list(1)
l1.traverse_the_list()
