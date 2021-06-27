#Level_Order_Trcversal of a Tree...

#Let's create a node first!
#Level order traversal can be implemented using queue. 
#Initially a node has been created which contains the root , it's left child , it's right child...

from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def Level_Order(self , root):
        #Let's create an empty queue.
        self.Q = deque()
        t = root
        print(t.data)
        self.Q.append(t)
        while (self.Q):
            t = self.Q.popleft()
            if t.left != None:
                print(t.left.data)
                self.Q.append(t.left)
            if t.right != None:
                print(t.right.data)
                self.Q.append(t.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
BT = BinaryTree()
BT.Level_Order(root)


