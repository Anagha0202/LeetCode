# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        node can appear 0,1 times
        root not need in path
        path_sum = sum(node.val)

        at each node, 
        max(node.val, left_branch+node.val+right_branch)
        return (node.val+left_branch, node.val+right_branch)
        if leaf node: return node.val
        t: O(n)
        s: O(1)
        """
        max_val = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            max_val[0] = max(max_val[0], left+node.val+right)
            return max(left+node.val, right+node.val)
        
        dfs(root)
        return max_val[0]