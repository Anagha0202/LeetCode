# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def searchTree(originalNode, clonedNode, targetNode):
            if not originalNode:
                return None
            if originalNode.val == target.val:
                return clonedNode
            return (searchTree(originalNode.left, clonedNode.left, targetNode) or 
            searchTree(originalNode.right, clonedNode.right, target))
        
        return searchTree(original, cloned, target)