# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    moves_made = 0
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            
            node.val = node.val + (left+right)
            self.moves_made += (abs(left) + abs(right))

            if node.val == 1:
                return 0
            elif node.val == 0:
                return -1
            else:
                return (node.val-1)
        
        ans = helper(root)
        return self.moves_made