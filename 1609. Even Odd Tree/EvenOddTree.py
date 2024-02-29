# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # Level order traversal => BFS. Mark the beginning of each level with the level number. Level number identifies if checking is (even & desc) or (odd & asc)
        queue = collections.deque([root])
        level = 0
        while queue:
            prev = -math.inf if (level%2==0 or level==0) else math.inf
            # prev = 0 if (level%2==0 or level==0) else (math.pow(10,6)+1)
            for _ in range(len(queue)):
                node = queue.popleft()
                cur = node.val
                # even level 
                if level==0 or level%2==0:
                    # odd elements and asc 
                    if cur%2==0 or prev>=cur:
                        return False
                # odd level 
                else:
                    # even elements and desc 
                    if cur%2!=0 or prev<=cur:
                        return False

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

                prev = cur
            level += 1
        
        return True
