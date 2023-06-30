# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def DFS(leftTree, rightTree):
            # if both trees are null i.e leaf nodes => symmetric
            if not leftTree and not rightTree:
                return True            
            # if one of them is null i.e one is a leaf node => non symmetric
            if not leftTree or not rightTree:
                return False
            # if both has values, check the values and check opposite subtrees
            return ((leftTree.val == rightTree.val) and
            (DFS(leftTree.left, rightTree.right)) and 
            (DFS(leftTree.right, rightTree.left)))

        return DFS(root.left, root.right)