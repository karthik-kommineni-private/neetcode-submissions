# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        #logic/idea is create a node, left and right for each node
        root = TreeNode(preorder[0]) #always first element in preorder
        mid = inorder.index(root.val) #mid of inorder list

        #element index from preorder - always divide inorder list as left subtree and right subtree

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root


