#Function to find the sum of all Nodes in a Binary Tree.
""" 
Example: 
Input : 
Level Order : 12345
Output : 15
"""
def sumBT(root):
    #code
    if root is None:
        return 0
    return root.data + sumBT(root.left) + sumBT(root.right)
