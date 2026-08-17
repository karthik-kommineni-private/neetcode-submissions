# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        rightHeight, leftHeight = 0,0 
        if not root:
            return True

        if root.left:
            leftHeight = self.get_height(root.left)

        if root.right:
            rightHeight = self.get_height(root.right) 

        if  abs(rightHeight-leftHeight) > 1: 
            return False  
        else:
            return True    





    def get_height(self, root) -> int:
        left, right = 0, 0
        if not root:
            return 0

        if root.left:
            left = self.get_height(root.left) 

        if root.right:
            right = self.get_height(root.right)   

        return max(left,right)+1            
        







"""
abs(leftheight - rightHeight) > 1 -> return False


"""

