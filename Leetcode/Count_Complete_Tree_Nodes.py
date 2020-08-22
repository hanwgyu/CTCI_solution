# Solution : 맨 밑 level에서 Binary Search 진행.
# Time : O(logN*logN), Space : O(1)


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def findDepth(root: TreeNode) -> int:
            ans, node = -1, root
            while node:
                node, ans = node.left, ans + 1
            return ans

        def nodeExist(idx: int):
            node, idx_rev = root, 0
            for i in range(self.H):
                idx, idx_rev = (
                    idx // 2,
                    idx_rev | (idx % 2) << (self.H - 1 - i),
                )
            for i in range(self.H):
                idx_rev, go_right = idx_rev // 2, idx_rev % 2
                node = node.right if go_right else node.left
                if not node:
                    return False
            return True

        if not root:
            return 0
        self.H = findDepth(root)
        l, r = 0, 2 ** self.H - 1
        while l <= r:
            # binary search 결과 l이 가장 마지막 노드의 다음 index, r이 가장 마지막 노드의 index를 가리키게됨.
            m = (l + r) // 2
            if nodeExist(m):
                l = m + 1
            else:
                r = m - 1
        return 2 ** self.H + r
