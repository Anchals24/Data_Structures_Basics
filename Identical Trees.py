#Program to check if two trees are identical.....!!!

#Approach... 1 Using Level-Order...


from collections import deque
class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __identity__(self , root1 , root2):
        self.Q = deque()
        #print(root1)
        #print(root2)
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        self.Q.append((root1 , root2))
        Flag = True
        while (self.Q):
            temp1 , temp2 = self.Q.popleft()
            #print(temp1.data)
            #print(temp2.data)
            if temp1.data != temp2.data:
                #print ("Hello")
                Flag = False
                break
            if temp1.left != None and temp2.left != None:
                self.Q.append((temp1.left , temp2.left))
            if temp1.right != None and temp2.right != None:
                self.Q.append((temp1.right , temp2.right))
            if (temp1.left == None and temp2.left != None) or (temp1.left != None and temp2.left == None):
                Flag = False
                #print("Hello")
                break
            if (temp1.right == None and temp2.right != None) or (temp1.right != None and temp2.right == None):
                Flag = False
                break
            
        if Flag == True:
            return True
        else:
            return False
        
        #Approach 2... using Recursion

    def isIdentical(self,root1, root2):
        # Code here
        if root1 == None and root2 == None:
            return True
        if root1 != None and root2 != None:
            return ((root1.data == root2.data) and self.isIdentical(root1.left , root2.left) and self.isIdentical(root1.right , root2.right))
        return False

BTree = BinaryTree()
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
#root1.left.left = Node(4)
#root1.left.right = Node(5)
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
#root2.left.left = Node(4)
#root2.left.right = Node(5)

print(BTree.__identity__(root1 , root2))
print(BTree.isIdentical(root1 , root2))

