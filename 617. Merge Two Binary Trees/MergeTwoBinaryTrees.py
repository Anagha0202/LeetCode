# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def BFS(root1, root2):
            if not root1 and not root2:
                return None
            if root1 and not root2:
                return root1
            if not root1 and root2:
                return root2
            
            root1.val = root1.val+root2.val
            root1.left = BFS(root1.left, root2.left)
            root1.right = BFS(root1.right, root2.right)
            return root1

            # val1 = root1.val 
            # val2 = root2.val 

            # node = TreeNode(val1+val2)
            # node.left = BFS(root1.left, root2.left)
            # node.right = BFS(root1.right, root2.right)

            # return node
        return BFS(root1, root2)