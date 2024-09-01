# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # t: O(v+e)
        # s: O(n)
        def dfs(node, result):
            if not node:
                return 0
            left, right = dfs(node.left, result), dfs(node.right, result)
            position = max(left, right)
            if len(result) == position:
                result.append([]) 
            result[position].append(node.val)
            return position + 1

        result = []
        dfs(root, result)
        return result