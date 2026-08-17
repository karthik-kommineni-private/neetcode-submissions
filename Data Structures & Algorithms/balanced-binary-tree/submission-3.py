# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        balanced = self.checkHeightAndBalance(root) 

        return balanced != -1





    def checkHeightAndBalance(self,root):

        if not root:
            return 0

        left = self.checkHeightAndBalance(root.left)
        right = self.checkHeightAndBalance(root.right)

        if left == -1 or right == -1 or abs(left-right)>1:
            return -1

        return max(left,right)+1







        







"""
abs(leftheight - rightHeight) > 1 -> return False

challenge : pass throught all nodes and find heights of subtrees for each node
-hence for each node - find heights is o(n) and have to do for all nodes so o(n2)


- going to all nodes is repeating
- hence do one pass solution which bottom approach 
- during bottom up - we determine isblanced from bottom while determining heights itself


"""

