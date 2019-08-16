# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution : 'Serialize and Deserialize Binary Tree'와 다르게 NULL Node를 '#'으로 표시해주지 않아도됨.
# Deserialize과정에서 값이 정의된 범위에 속하는지 확인하여 속하지 않으면 pass함.

from collections import deque

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preOrder(node):
            if not node:
                return
            data.append(str(node.val))
            preOrder(node.left)
            preOrder(node.right)
        data = []
        preOrder(root)
        return '!'.join(data)
                    
    def deserialize(self, data):
        def preOrder(minVal, maxVal):
            if not vals or vals[0] <= minVal or maxVal <= vals[0]:
                return
            val = vals.popleft()
            node = TreeNode(val)    
            node.left = preOrder(minVal, val)
            node.right = preOrder(val, maxVal)
            return node
        if not data:
            return None
        vals = deque(int(val) for val in data.split('!'))
        return preOrder(float('-inf'), float('inf'))
   
