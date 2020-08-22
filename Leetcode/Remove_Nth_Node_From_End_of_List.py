# Time Complexity : O(n)
# Solution : Count가 n이 넘어갔을때 부터 새로운 Pointer를 head에서 움직이기 시작해, 타겟 노드를 찾아 제거
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return None
        if n == 0:
            return head

        # Find target node
        node, before_target = head.next, None
        count = 0
        while node:
            node = node.next
            count += 1
            if count == n:
                before_target = head
            elif count > n:
                before_target = before_target.next

        # when target is head
        if not before_target:
            return head.next

        # Remove node
        before_target.next = before_target.next.next

        return head
