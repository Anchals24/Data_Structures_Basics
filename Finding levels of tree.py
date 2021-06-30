from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree:
    def levels(self , root):
        self.Q = deque()
        temp = root
        T = (temp , 1)
        self.Q.append(T)
        while(self.Q):
            temp = self.Q.popleft()
            if temp[0].left != None:
                left = (temp[0].left , temp[1] + 1)
                self.Q.append(left)
            if temp[0].right != None:
                right = (temp[0].right , temp[1] + 1)
                self.Q.append(right)
        
Btree = Binary_Tree()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.left.left.right = Node(8)
#Btree.preorder(root)
Btree.levels(root)
