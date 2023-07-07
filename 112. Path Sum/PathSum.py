# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def DFS(node, targetsum):
            if not node:
                return False
            targetsum-=node.val
            if not node.left and not node.right:
                return targetsum==0
            return (DFS(node.left, targetsum) or DFS(node.right, targetsum))

        return DFS(root, targetSum)            
