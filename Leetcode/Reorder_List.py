# Solution : 절반 노드로 나누고, 뒤쪽 노드를 reverse한후, 두 노드를 합침.
# Time : O(N), Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Tuple


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def seperateList(head: ListNode) -> Tuple[ListNode, ListNode]:
            # find length
            node, l = head, 0
            while node:
                node, l = node.next, l + 1
            # seperate nodes
            node = head
            for _ in range(l // 2 - 1):
                node = node.next
            mid = node.next
            node.next = None
            return (head, mid)

        def reverseList(head: ListNode) -> ListNode:
            if not head.next:
                return head
            cur, last = head, None
            while cur:
                tmp = cur.next
                cur.next = last
                last = cur
                cur = tmp
            return last

        def mergeList(first: ListNode, second: ListNode) -> ListNode:
            head = ListNode()
            node = head
            while first or second:
                if first:
                    node.next = first
                    node = node.next
                    first = first.next
                    if not second:
                        break
                if second:
                    node.next = second
                    node = node.next
                    second = second.next
                    if not first:
                        break
            return head.next

        if not head or not head.next:
            return
        first, second = seperateList(head)
        second = reverseList(second)
        return mergeList(first, second)
