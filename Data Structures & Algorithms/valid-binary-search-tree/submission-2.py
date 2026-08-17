# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # EVERY NODE - is valid - when its range is btw its parent
        return self.helper(root, -float('inf'), float('inf'))




    #every node must be within its bounds
    #left node - parent left and parent val
    def helper(self, node, left, right):
        if node is None:
            return True
        if not left<node.val<right:   
            return False

        left_node_bool = self.helper (node.left, left,node.val)
        right_node_bool = self.helper(node.right, node.val, right) 

        return left_node_bool and right_node_bool



"""
Logic idea:
- bounds keep updating
- for left nodes right keeps updating and vice versa


"""       


        