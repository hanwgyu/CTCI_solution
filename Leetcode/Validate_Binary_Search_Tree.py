# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution : Check with in-order traversal. If current value becomes smaller than previous value, then return False.
# Time : O(N), Space : O(Height)

class Solution(object):
    def isValidBST(self, root):
        def inOrder(node):
            if not node:
                return True
            if not inOrder(node.left):
                return False
            nonlocal val
            if val >= node.val:
                return False
            val = node.val
            if not inOrder(node.right):
                return False
            return True
        val = float('-inf')
        return inOrder(root)
        
