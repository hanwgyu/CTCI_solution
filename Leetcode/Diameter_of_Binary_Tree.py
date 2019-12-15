# Solution : Traverse하면서 왼쪽, 오른쪽 child의 최대 길이를 리턴받아 현재 노드를 거치는 최대 길이를 구함.
# Time : O(N), Space : O(H)
# 'Minimum Height Trees' 문제의 쉬운 버전.

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def maxLength(node: TreeNode) -> None:
            nonlocal ans
            if not node:
                return 0
            l = maxLength(node.left)
            r = maxLength(node.right)
            ans = max(ans, l+r)
            return max(l,r)+1   
        ans = 0
        maxLength(root)
        return ans
