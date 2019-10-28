# Time : O(N), Space : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        before, front, back, head = None, head, head.next, head.next
        while front and back:
            front.next, back.next = back.next, front
            if before: before.next = back
            front, back, before = front.next, front.next.next if front.next else None, front
        return head
            
