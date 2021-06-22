""" 
Creating a binary tree
Let's start by creating a Node first.

As a tree contains "Left" and "Right" child..
We will simply create a node.. which will contain Left and Right.
"""

#Creating a Node first...

class Node:
    def __init__ (self , data):
        self.data = data
        self.left = None
        self.right = None

#Now let's create a Binary Tree and try to implement various traversal techniques...

class Binary_Tree:

    """
        Preorder Traversing : +AB  
        ROOT -> LEFT -> RIGHT 

    """

    def __preorder__(self, root):
        
        if root is None:
            return
        print(root.data)
        self.__preorder__(root.left)
        self.__preorder__(root.right)

    """
        Inorder Traversing : A+B  
        LEFT -> ROOT -> RIGHT 
        
    """

    def __inorder__(self , root):
        if root is None:
            return
        self.__inorder__(root.left)
        print(root.data)
        self.__inorder__(root.right)
    
    """
        Postorder Traversing : AB+
        LEFT -> RIGHT -> ROOT
        
    """
    
    def __postorder__(self, root):
        if root is None:
            return
        self.__postorder__(root.left)
        self.__postorder__(root.right)
        print(root.data)


# So, Let's create a Complete // proper // Full- binary tree.
root = Node("A")
root.left = Node("B")
root.right = Node ("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

btree = Binary_Tree()
btree.__preorder__(root)
#btree.__postorder__(root)
#btree.__inorder__(root)

        
