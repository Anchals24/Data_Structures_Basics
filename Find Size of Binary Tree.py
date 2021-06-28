#To calculate the size of a tree. 
#How many nodes are present in a Tree.


def getSize(node):
    # code here
    if node is None:
        return 0
    return 1 + getSize(node.left) + getSize(node.right)


#Note : This is just a function to count total Nodes. To run this , Binary Tree must be created first.........!!!