# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        def preorderDFS(node):
            if not node:
                return 
            traversal.append(node.val)
            preorderDFS(node.left)
            preorderDFS(node.right) 

        preorderDFS(root)
        return traversal