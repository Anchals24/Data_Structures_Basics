

from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def Level_Order(self , root):
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


