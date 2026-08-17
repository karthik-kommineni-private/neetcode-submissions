# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.total_max_path_sum = float('-inf')
        self.dfs(root)
        return self.total_max_path_sum

    def normalize(self, node_val: int) -> int:
        if node_val <= 0:
            return 0   
        else:
            return node_val    

    def dfs(self, root: Optional[TreeNode])-> int:
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        maxPathSumAtNode = root.val + self.normalize(left) + self.normalize(right)
        self.total_max_path_sum = max(maxPathSumAtNode,self.total_max_path_sum)
        return root.val + max(self.normalize(left), self.normalize(right))