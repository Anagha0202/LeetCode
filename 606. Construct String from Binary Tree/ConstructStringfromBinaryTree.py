# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        binaryString = ""
        def preorder(node):
            nonlocal binaryString
            if not node:
                return ""
            binaryString+=str(node.val)
            if node.left or node.right: 
                binaryString+="(" 
                if node.left and not node.right:
                    preorder(node.left)
                elif not node.left and node.right:
                    binaryString+=")("
                    preorder(node.right)
                else:
                    preorder(node.left)
                    binaryString+=")("
                    preorder(node.right)
                binaryString+=")"
            return binaryString
        
        return preorder(root)
