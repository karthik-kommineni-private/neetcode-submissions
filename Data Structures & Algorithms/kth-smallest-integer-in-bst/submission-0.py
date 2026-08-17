# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.res = 0
        self.dfs(root)
        return self.res


    def dfs(self,node):
        if node is None:
            return 
        self.dfs(node.left)
        self.counter+=1
        if(self.counter == k):
            self.res = node.val
            return
        self.dfs(node.right) 







"""
- in order
- c

if root none - return
dfs(left)
c +=1 
dfs(right)



"""

        