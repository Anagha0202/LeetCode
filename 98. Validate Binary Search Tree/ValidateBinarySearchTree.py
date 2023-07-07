# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def DFS(node, lower, upper):
            if not node:
                return True
            if node.val<=lower or node.val>=upper:
                return False
            return DFS(node.left, lower, node.val) and DFS(node.right, node.val, upper)
        return DFS(root, float("-inf"), float("inf"))