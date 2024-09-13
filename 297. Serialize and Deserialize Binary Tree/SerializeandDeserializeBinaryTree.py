# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    Use preorder traversal to build the serialized string. 
    root, left, right 
    if null node is reached, add Null to the serialization

    Use class variable to track the index in deserialization
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # t: O(n)
        # s: O(n)
        serial = []
        def dfs(node):
            if not node:
                serial.append("N,")
                return 
            
            serial.append(str(node.val)+ ",")
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        
        return ''.join(serial)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # t: O(n)
        # s: O(n)
        deserial = data.split(",")
        self.index = 0

        def dfs():
            if deserial[self.index]=="N":
                self.index+=1
                return None
            
            node = TreeNode(int(deserial[self.index]))
            self.index+=1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))