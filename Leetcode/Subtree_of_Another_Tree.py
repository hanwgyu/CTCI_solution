# Solution : Recursive하게 s의 모든 subtree에 대해 t와 똑같은지 검사.
# Time : O(ST), Space : O(h(T))

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(m: TreeNode, n: TreeNode) -> bool:
            if not m and not n:
                return True
            elif not m or not n:
                return False
            if m.val == n.val and isSame(m.left, n.left) and isSame(m.right, n.right):
                return True
            return False
        return s and (isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
