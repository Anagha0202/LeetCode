# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # traverse only the nodes that are potentially teh LCA
        # t: O(logn) - visiting only one node in a height
        # s: O(1)

        lca_node = root
        while lca_node:
            if p.val<lca_node.val and q.val<lca_node.val:
                lca_node = lca_node.left
            elif p.val>lca_node.val and q.val>lca_node.val:
                lca_node = lca_node.right
            elif p.val==lca_node.val or q.val==lca_node.val:
                return lca_node
            else:
                return lca_node