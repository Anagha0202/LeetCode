# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # Approach: Least Common Ancestor - DFS
        # Each leaf node: returns 1
        # Each non-leaf node: return list of all connected leaf nodes that can be further considered given the distance constraint
        count = 0

        def dfs(node):
            nonlocal count
            if not node:
                return []
            
            # if leaf node
            if not node.left and not node.right:
                return [1]
            
            # non-leaf node
            left = dfs(node.left)
            right = dfs(node.right)

            # current node is LCA node so count how many pairs of left and right leaf nodes are good i.e left+right<=distance holds good
            for l in left:
                for r in right:
                    if l+r<=distance:
                        count+=1
            
            # find the number of leaf nodes from either side that can be taken further into consideration
            leafs = []
            for n in left+right:
                if n+1 < distance: # not <= Eg. if distance = 3 and left branch returns [3] then it does not give room to combine with right branch
                    leafs.append(n+1)
            return leafs
        
        dfs(root)
        return count
            