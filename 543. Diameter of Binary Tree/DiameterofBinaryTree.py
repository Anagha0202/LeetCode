# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxdiameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def DFS(node):
            if not node:
                return [0,-1]
            leftD, leftH = DFS(node.left)
            rightD, rightH = DFS(node.right)
            diameter = leftH + rightH + 2
            height = max(leftH, rightH) + 1
            self.maxdiameter = max(self.maxdiameter, diameter)
            return [diameter, height]
        DFS(root)
        return self.maxdiameter