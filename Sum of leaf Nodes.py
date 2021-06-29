#Sum of leaf Nodes...............................................!!!!
#Leaf Nodes are the nodes of a tree which does not have any child.

def sumLeaf(root):
    '''
    :param root: root of given tree.
    :return: sum of leaf nodes
    '''
    # code here
    if root is None:
        return 0
    if root.left == None and root.right == None:
        return root.data
    return sumLeaf(root.left) + sumLeaf(root.right)