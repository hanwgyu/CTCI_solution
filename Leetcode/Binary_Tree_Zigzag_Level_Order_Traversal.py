# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution : Use two stack. Change traversal direction (left -> right or right -> left) at every level.
# Time : O(N), Space : O(N)
class Solution(object):
    def zigzagLevelOrder(self, root):
        def traverseStack(src, dest, left_to_right):
            ans = []
            while src:
                node = src.pop()
                ans.append(node.val)
                if left_to_right and node.left:
                    dest.append(node.left)    
                if node.right:
                    dest.append(node.right)
                if not left_to_right and node.left:
                    dest.append(node.left)
            return ans
        
        if not root:
            return None
    
        stack_ltor, stack_rtol, ans = [root], [], []
        while stack_ltor or stack_rtol:
            a = []
            if stack_ltor:
                a = traverseStack(stack_ltor, stack_rtol, True)
            else:
                a = traverseStack(stack_rtol, stack_ltor, False)
            if a:
                ans.append(a)

        return ans
        
