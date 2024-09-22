# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, path, target):
            if node.val == target:
                return True
            if node.left and dfs(node.left, path, target):
                path.append("L")
            elif node.right and dfs(node.right, path, target):
                path.append("R")
            return path
        
        start_path, end_path = [], []
        dfs(root, start_path, startValue)
        dfs(root, end_path, destValue)

        while start_path and end_path and start_path[-1]==end_path[-1]:
            start_path.pop()
            end_path.pop()
        
        return "".join("U"*len(start_path)) + "".join(end_path[::-1])