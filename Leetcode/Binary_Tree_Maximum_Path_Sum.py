# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution : 노드들을 Post-Order Traversal하면서, 해당 노드를 root로 하는 트리에서 해당 노드를 포함하는 maximum path sum을 구함.
# 그 중에서 가장 큰 값을 리턴.
# Time : O(N), Space : O(H)


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def postOrder(
            node: TreeNode,
        ) -> int:  # 노드 포함하면서 한쪽 child과만 연결되는 최대값을 리턴.
            if not node:
                return 0
            l_max = postOrder(node.left)
            r_max = postOrder(node.right)
            max_sum = node.val
            if l_max > 0:
                max_sum += l_max
            if r_max > 0:
                max_sum += r_max
            nonlocal ans
            ans = max(ans, max_sum)
            return node.val + max(l_max, r_max, 0)

        ans = float("-inf")
        postOrder(root)
        return ans
