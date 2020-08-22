# Solution : 절반 이후의 리스트를 Reverse시켜서 앞쪽 리스트와 합침.
# Time : O(N), Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverseList(head: ListNode) -> ListNode:
            if not head:
                return None
            post, cur, pre, = None, head, None
            while cur:
                post = cur.next
                cur.next = pre
                pre, cur = cur, post
            return pre

        if not head:
            return None
        # Find length
        N = 1
        cur = head
        while cur.next:
            N, cur = N + 1, cur.next
        # Find Mid and sperate two lists
        cur = head
        for i in range((N - 1) // 2):
            cur = cur.next
        rev_head, cur.next = cur.next, None
        # reverse second list
        rev_head = reverseList(rev_head)
        # merge two lists
        post, cur, rev_post, rev_cur = None, head, None, rev_head
        while cur and rev_cur:
            post, rev_post = cur.next, rev_cur.next
            cur.next = rev_cur
            rev_cur.next = post
            cur, rev_cur = post, rev_post
        return head
