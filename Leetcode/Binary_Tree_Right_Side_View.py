# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution : Use pre-order. Save node.val to ans[Height] at every node.
# Time: O(N), Space : O(Height)

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def preOrder(node: TreeNode, height: int):
            if not node:
                return
            if len(ans) < height + 1:
                ans.append(node.val)
            else:
                ans[height] = node.val
            preOrder(node.left, height + 1)
            preOrder(node.right, height + 1)
            
        ans = []
        preOrder(root, 0)
        return ans
