# Solution 1. Time : O(N), Space: O(H)


class Solution:
    def sumRootToLeaf_1(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, s: int):
            if not node:
                return
            s = s * 2 + node.val
            if not node.left and not node.right:
                self.ret += s
            dfs(node.left, s)
            dfs(node.right, s)

        self.ret = 0
        dfs(root, 0)
        return self.ret
