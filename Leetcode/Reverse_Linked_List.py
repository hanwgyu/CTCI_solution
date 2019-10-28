# Time : O(N), Space : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        front, back, target = head, head, head.next
        while target:
            back.next, target.next = target.next, front
            front, target = target, back.next
        return front
