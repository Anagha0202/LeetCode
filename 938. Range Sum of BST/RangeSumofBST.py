# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    rangeSum = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def sumTree(node, low, high):
            if not node:
                return 
            if node.val>high:
                sumTree(node.left, low, high)
            elif node.val<low:
                sumTree(node.right, low, high)
            else:
                self.rangeSum+=node.val
                sumTree(node.left, low, high)
                sumTree(node.right, low, high)

        sumTree(root, low, high)
        return self.rangeSum
        
        # def approach1():
        #     sumList = []
        #     def DFS(node, low, high):
        #         if not node:
        #             return
        #         if low<=node.val<=high:
        #             sumList.append(node.val)
        #         DFS(node.left, low, high)
        #         DFS(node.right, low, high)
            
        #     DFS(root, low, high)
        #     return sum(sumList)
