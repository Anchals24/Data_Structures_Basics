#Function to count the NON-LEAF Nodes of a Tree.

#Non-Leaf Nodes are the nodes which have child.



class Solution:
    def countNonLeafNodes(self, root):
        # add code here
        if root is None:
            return 0
        elif root.left == None and root.right == None:
            return 0
        return 1 + self.countNonLeafNodes(root.left) +self.countNonLeafNodes(root.right)