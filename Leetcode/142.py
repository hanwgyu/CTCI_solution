class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        fast, slow를 이동해서 만나면, slow를 head로 보내 다시 만나게 되는 지점이 cycle의 시작점...
        
        너무 천재적이고 알수가 없다.

        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
