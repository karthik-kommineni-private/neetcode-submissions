# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.check_good_node(root, 0)
        return self.count        

    def check_good_node(self,node: TreeNode, max_ele: int):  
        if not node:
            return  
        new_max_ele = max(max_ele, node.val)
        if node.val > max_ele:
            self.count+=1
        if node.left:
            self.check_good_node(node.left,new_max_ele)
        if node.right:
            self.check_good_node(node.right,new_max_ele) 

        