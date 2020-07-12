# Solution : dfs통해 모든 노드를 순회. 각 레벨의 가장 왼쪽 index(위쪽부터 0, 1, 2,... 증가) 저장해놓고 maximum width를 업데이트함.
# Time : O(N), Space: O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node, level, idx):
            if not node:
                return
            if level not in self.left_idx:
                self.left_idx[level] = idx
                
            self.max_width = max(self.max_width, idx - self.left_idx[level] + 1)
            dfs(node.left, level + 1, 2 * idx)
            dfs(node.right, level + 1, 2 * idx + 1)
        self.left_idx = defaultdict(int)
        self.max_width = 0
        dfs(root, 0, 0)
        return self.max_width
