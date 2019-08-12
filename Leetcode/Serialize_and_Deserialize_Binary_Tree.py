# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution : Serialize in pre-order. Express NULL as '#' and a node seperator as '!'.
# Use stack to deserialize.
# ex)  
#    10
#   /  \
#  -1   5
#  /    
# 3                    => 10!-1!3!#!#!#!5!#!#!

class Codec:
    def preOrder(self, node, data):
        if not node:
            data.append('#!')
            return
        data.append(str(node.val)+'!')
        self.preOrder(node.left, data)
        self.preOrder(node.right, data)
    
    
    # Time : O(N), Space : O(N)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        self.preOrder(root, data)
        return ''.join(data)
        

    # Time : O(N), Space : O(N)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
                
        root, stack, i = None, [], 0
        while i < len(data):
            if data[i] == '#':
                node = None
                i += 1
            elif data[i] == '-':
                start = i
                while data[i] != '!':
                    i += 1
                node = TreeNode(data[start:i])
            else :
                start = i
                while data[i] != '!':
                    i += 1
                node = TreeNode(data[start:i])
            if not stack:
                root = node
            else:
                s = stack.pop()
                while s[1] == 0:
                    s = stack.pop()      
                if s[1] == 2:
                    s[0].left = node
                    stack.append((s[0], 1)) 
                elif s[1] == 1:
                    s[0].right = node
                    stack.append((s[0], 0))
            if node:
                stack.append((node, 2))
            i += 1
        return root        
