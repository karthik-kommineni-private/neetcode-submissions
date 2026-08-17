# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0

        #calculate max height
        def dfs(curr):
            left,right = 0 , 0
            if not curr:
                return 0
            if curr.left:    
                left = dfs(curr.left)  
            if curr.right:    
                right = dfs(curr.right) 

            self.max_dia = max(self.max_dia, left+right)

            return max(left,right)+1

        dfs(root)
        return self.max_dia    











"""
- calculate diameter at each node = max(left)+max(right)
- calcutae result = max diameter -> so max(dia) at each node
"""

        