#Function to delete the Alternate Nodes of a Linkedlist!


def alternative_delete(self):
        if self.head == None:
            return
        if self.head.next is None:
            return self.head.data
        else:
            temp = self.head
            change = temp
            while (temp):
                temp = temp.next
                temp2 = temp
                change.next = temp.next
                del(temp2)
                temp = change.next
                change = temp


