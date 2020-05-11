# Solution : 리스트의 중간지점을 root로 왼쪽, 오른쪽을 만듬.
# Recursive하게 동작시키고, 남은 갯수가 2개, 1개이면 Create하고 리턴.
# 처음에 길이를 구하고, 왼쪽, DFS방식으로 가장 앞쪽 줄부터 추가하도록. (모든 bst노드의 왼쪽은 현재보다 작은값들만 있음.)
# Time : O(N), Space : O(logN)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def createBST(i: int) -> TreeNode:
            if i == 0:
                return None
            q, r = (i-1)//2, (i-1)%2
            l = createBST(q+r)
            node = TreeNode(self.cur.val)
            self.cur = self.cur.next
            r = createBST(q)
            node.left, node.right = l, r
            return node
        # Get length
        L = 0
        node = head
        while node:
            L, node = L+1, node.next
        self.cur = head
        return createBST(L)
