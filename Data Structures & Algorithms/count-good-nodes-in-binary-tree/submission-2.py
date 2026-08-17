# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
       self.res = 0
       self.dfs(root, root.val)
       return self.res

    def dfs(self, node, max_val):
        if not node:
            return
        
        if node.val >= max_val:
            self.res += 1
        
        max_val = max(max_val, node.val)
        
        self.dfs(node.left, max_val)
        self.dfs(node.right, max_val)


           

        