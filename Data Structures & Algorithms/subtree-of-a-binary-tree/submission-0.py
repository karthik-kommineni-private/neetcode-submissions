# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        elif not root and subRoot: 
            return False
        elif root and not subRoot: 
            return False   

        if root.val == subRoot.val:
            left_bool = self.isSubtree(root.left, subRoot.left) 
            right_bool = self.isSubtree(root.right, subRoot.right)  
            return left_bool and right_bool
        else:
            left_bool = self.isSubtree(root.left, subRoot) 
            right_bool = self.isSubtree(root.right, subRoot)
            return left_bool or right_bool 

            
          
        