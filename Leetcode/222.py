# left child, right child의 height 를 비교해, 같으면 오른쪽 child로 이동, 다르면 왼쪽 child로 이동해야 가장 마지막 노드에 도달할 수 있다.
# Time : O((logN)^2), Space: O(logN)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def height(node: TreeNode) -> int:
            if not node:
                return 0
            return 1 + height(node.left)

        def dfs(node: TreeNode, n: int) -> int:
            if not node:
                return n//2
            if height(node.left) == height(node.right):
                return dfs(node.right, 2*n+1)
            else:
                return dfs(node.left, 2*n)
        return dfs(root, 1)
