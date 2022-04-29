#Problem_Statement

"""
Problem1: Height of a Binary Tree.
Given a binary tree, find its height.

"""

#or

"""

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""
#There's same way to find the height/depth of the Binary Tree.

def maxDepth(self, root):
  #basecase: if there exists no root, height will be 0. Hence, put it as the base condition.
  if root is None:
    return 0
  #Calculate the depth/height for the left subtree using recursive calls
  leftdepth = self.maxDepth(root.left)
  #Calculate the depth/height for the right subtree using recursive calls
  rightdepth = self.maxDepth(root.right)
  #now post adding 1(for the root node), add max of left subtree/ right subtree.
  return 1 + max(leftdepth, rightdepth)     



"""
Problem2: Minimum depth of a tree.

Problem Statement: 
"""


def minDepth(self, root):
  #basecase: if there exists no root, min depth will be 0. Hence, put it as the base condition.
  if root is None:
    return 0
  #Calculate the depth/height for the left subtree using recursive calls
  leftdepth = self.minDepth(root.left)
  #Calculate the depth/height for the right subtree using recursive calls
  rightdepth = self.minDepth(root.right)
  #when left subtree doesn't exists. Then, simply add 1 to the min depth of right subtree.
  if left == None:
    return 1 + right
  #when right subtree doesn't exists. Then, simply add 1 to the min depth of left subtree.
  if right == None:
    return 1 + left
  #now post adding 1(for the root node), add min of left subtree/ right subtree.
  return 1 + min(leftdepth, rightdepth)
