# Time Complexity : O(n), Space Complexity : O(1)
# Solution : 움직이는 속도가 다른 두 노드를 두어 언젠가 동일해지면 loop가 존재하는 것.
class Solution(object):
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    
    def hasCycle(self, head):
        node_fast = head
        node_slow = head

        while node_fast:
            node_fast = node_fast.next
            if not node_fast:
                break
            node_fast = node_fast.next
            node_slow = node_slow.next
            if node_fast == node_slow:
                return True

        return False
