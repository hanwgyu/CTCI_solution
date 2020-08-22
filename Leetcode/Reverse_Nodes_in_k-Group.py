# Time : O(N), Space : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseK(before: ListNode, start: ListNode, k: int):
            if k < 2:
                return (start, start)
            front, back, target = start, start, start.next
            for _ in range(k - 1):
                target.next, back.next = front, target.next
                front, target = target, back.next
            if before:
                before.next = front
            return (front, back)

        if not head:
            return None
        # 노드 전체 길이 계산
        node, n = head, 0
        while node:
            node, n = node.next, n + 1

        start, before = head, None
        for i in range(n // k):
            (front, before) = reverseK(before, start, k)
            if i == 0:
                head = front
            start = before.next
        return head
