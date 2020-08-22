# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution : Serialize in pre-order. Express NULL as '#' and a node seperator as '!'.
# Deserialize : 1) Recursive 2) Use stack
# ex)
#    10
#   /  \
#  -1   5
#  /
# 3                    => 10!-1!3!#!#!#!5!#!#


class Codec:
    # Time : O(N), Space : O(N)
    def serialize(self, root):

        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def preOrder(node, data):
            if not node:
                data.append("#")
                return
            data.append(str(node.val))
            preOrder(node.left, data)
            preOrder(node.right, data)

        data = []
        preOrder(root, data)
        return "!".join(data)

    def deserialize(self, data):
        def preOrder():
            val = next(it)
            if val == "#":
                return None
            node = TreeNode(val)
            node.left = preOrder()
            node.right = preOrder()
            return node

        it = iter(data.split("!"))
        return preOrder()

    # Time : O(N), Space : O(N)
    def deserialize_2(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        root, stack = None, []
        a = data.split("!")
        for val in a:
            if val == "#":
                node = None
            else:
                node = TreeNode(val)
            if not stack:
                root = node
            else:
                s = stack.pop()
                while stack and s[1] == 0:
                    s = stack.pop()
                if s[1] == 2:
                    s[0].left = node
                    stack.append((s[0], 1))
                elif s[1] == 1:
                    s[0].right = node
                    stack.append((s[0], 0))
            if node:
                stack.append((node, 2))
        return root
