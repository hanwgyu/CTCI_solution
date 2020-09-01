# Solution : 지우려는 노드의 predecessor를 찾아 값을 업데이트하고, 왼쪽 child로 내려가면서 recursive하게 반복.
# Time : O(H), Space: O(H)

# TODO) 값 변경말고, 노드 자체를 이동시키는 쉬운 방법 없나?
# 내려간 이후에 while문 안돌고 그냥 연결해주면 끝. Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # predecessor
            a = root.left
            while a.right:
                a = a.right
            root.val = a.val
            root.left = self.deleteNode(root.left, a.val)
        return root
