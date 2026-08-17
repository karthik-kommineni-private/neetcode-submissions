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

        if root.left and root.left.val > root.val:
            return False

        if root.right and root.right.val < root.val:
            return False    

        left = self.isValidBST(root.left)
        right = self.isValidBST(root.right)

        if not left: 
            return False
        return left and right    


        