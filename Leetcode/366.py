class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            O(N) / O(h)
        """
        res = []
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            h = max(dfs(node.left), dfs(node.right)) + 1
            if h > len(res):
                res.append([node.val])
            else:
                res[h-1].append(node.val)
            return h
        dfs(root)
        return res