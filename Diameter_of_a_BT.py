#Problem: Finding diameter of a Binary Tree.

"""
Problem Statement: Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

"""


"""
Pseudo Code/ Explanation: 

-- If root does not exists, diameter will be 0.
-- There are two cases:
        -- Path may pass from the root.
          calculate the height of left subtree and right subtree. Add them.
        -- Path may not pass from the root.
          find the max of left subtree diameter/ right subtree diameter of the tree.
          
-- return the maximum of the above cases. return max of(path which passes from the root, path which does not pass from the root).
"""
def height(root):
  if root is None:
    return 0
  return 1 + max(height(root.left), height(root.right))


def diameter(root):
  if root is None:
    return 0
  #let's make a recursive call on the left subtree to find left subtree diameter.
  ldia = diameter(root.left)
  #let's make a recursive call on the right subtree to find right subtree diameter.
  rdia = diameter(root.right)
  #calculate the height of left subtree 
  lh = height(root.left)
  #calculate the height of right subtree 
  rh = height(root.right)
  #when the path passes through the root.
  withroot = lh + rh
  #when the path does not passes through the root.
  withoutroot = max(ldia, rdia)
  #return the max of (path which passes from the root, path which does not pass from the root).
  return max(withroot, withoutroot)
