# Time : O(N), Space : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        pre, cur = head, head.next
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return head
