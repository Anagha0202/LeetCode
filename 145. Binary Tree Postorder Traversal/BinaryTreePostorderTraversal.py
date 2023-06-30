# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        def postorderDFS(node):
            if not node:
                return
            postorderDFS(node.left)
            postorderDFS(node.right)
            traversal.append(node.val)
        
        postorderDFS(root)
        return traversal