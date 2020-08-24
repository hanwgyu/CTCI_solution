# Solution 1 : Time : O(N), Space: O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves_1(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, is_left: bool):
            if not node:
                return
            if is_left and not node.left and not node.right:
                self.ret += node.val
            dfs(node.left, True)
            dfs(node.right, False)

        self.ret = 0
        dfs(root, False)
        return self.ret
