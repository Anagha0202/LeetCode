# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def DFS(leftTree, rightTree):
            if not leftTree and not rightTree:
                return True
            if not leftTree or not rightTree:
                return False
            return ((leftTree.val == rightTree.val) and 
            (DFS(leftTree.left, rightTree.left)) and
            (DFS(leftTree.right, rightTree.right)))
        
        return DFS(p, q)