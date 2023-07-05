# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #approach 2
        def balance(node):
            if not node:
                return [True, 0]
            left = balance(node.left)
            right = balance(node.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1])<=1
            return [balanced, max(left[1], right[1])+1]
        return balance(root)[0]

        #approach 1
        res = True
        def DFS(node):
            nonlocal res
            if not node:
                return -1
            leftH = DFS(node.left)
            rightH = DFS(node.right)
            if abs(leftH-rightH) > 1:
                res=False
            return max(leftH, rightH) + 1
        DFS(root)
        return res