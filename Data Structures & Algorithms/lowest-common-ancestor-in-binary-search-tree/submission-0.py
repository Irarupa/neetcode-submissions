# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if  root is None:
            return

        a = self.lowestCommonAncestor(root.left,p,q)
        b = self.lowestCommonAncestor(root.right,p,q)

        if root is p or root is q :
            return root

        if a is not None and b is not None:
            return root

        elif a is None :
            return b
        elif b is None:
            return a

        
        

