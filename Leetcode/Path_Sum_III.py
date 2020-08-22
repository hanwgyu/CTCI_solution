# Solution 1 : 각 node가 받을 수 있는 sum들을 리스트로 전달.
# Time : O(N^2)(Array 복사시간), Space : O(N^2)

# Solution 2 : root 부터 시작하는 sum들을 저장해나가면서, 각 sum들의 차이를 구해서 계산.
# Time : O(N), Space :O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import copy
from collections import defaultdict


class Solution:
    def pathSum_2(self, root: TreeNode, sum: int) -> int:
        def dfs(node: TreeNode, prev_sum: int):
            if not node:
                return
            curr_sum = prev_sum + node.val
            self.ret += d[curr_sum - sum]
            d[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            d[curr_sum] -= 1

        self.ret = 0
        d = defaultdict(int)
        d[0] = 1
        dfs(root, 0)
        return self.ret

    def pathSum_1(self, root: TreeNode, sum: int) -> int:
        def dfs(prev_sums: List[int], node: TreeNode):
            if not node:
                return
            for i in range(len(prev_sums)):
                prev_sums[i] += node.val
                if prev_sums[i] == sum:
                    self.ret += 1
            prev_sums.append(node.val)
            if node.val == sum:
                self.ret += 1
            dfs(copy.deepcopy(prev_sums), node.left)
            dfs(prev_sums, node.right)

        self.ret = 0
        dfs([], root)
        return self.ret
