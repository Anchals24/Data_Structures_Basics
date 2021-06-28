#To Find mirror of a Tree...!!!

""" 
Mirror of a Tree :
Input: Level order >> 1 2 3
Output : Level order >>  1 3 2
"""


class Solution:
    #Function to convert a binary tree into its mirror tree.
    def helper(self , root , ans):
        if root is None:
            return
        temp1 = root.left
        temp2 = root.right
        if temp1 != None or temp2 != None:
            root.left = temp2
            root.right = temp1
        self.helper(root.left , ans)
        ans.append(root.data)
        self.helper(root.right , ans)
        
            
    def mirror(self,root):
        # Code here
        ans = []
        self.helper(root , ans)
        return ans