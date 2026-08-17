# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True            
        left_val = self.get_value(root.left)    
        right_val = self.get_value(root.right)
        left_bool = self.isValidBST(root.left)
        right_bool=  self.isValidBST(root.right)

        return  left_val<root.val<right_val and left_bool and right_bool


    def get_value(self, node: TreeNode):
        if not node:
            return 0
        return node.val    

        