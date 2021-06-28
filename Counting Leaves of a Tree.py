#Function to count the leaves of a Binary Tree.
#Leaf Nodes are the Nodes which does not have any child.



def countLeaves(root):
    # Code here
    if root is None:
        return 0
    elif root.left == None and root.right == None:
        return 1
    return countLeaves(root.left) + countLeaves(root.right)


#Note : This is just a function to count Nodes. To run this , Binary Tree must be created first.........!!!