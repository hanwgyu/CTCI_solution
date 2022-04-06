class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        fast, slow를 이동해서 만나면, slow를 head로 보낸후 같은 속도로 이동해서 다시 만나게 되는 지점이 cycle의 시작점...
        
        너무 천재적이고 알수가 없다.

        그림 그리면 풀수있음. 항상 겹친다.
        1) 길이를 Cycle 시작점까지를 a, Cycle을 b로 놓는다. 
        2) Slow가 cycle 시작점에 도달했을때 Fast는 시작점에서 a-nb의 위치에 있게됨.
        3) Slow, Fast가 만나면 시작점에서 반대편으로 a-nb에 있게됨.
        4) Slow를 head로 보내고 a만큼을 이동시키면, Fast도 a-nb를 이동하면 시작점에 도달 그 이후 b를 n바퀴 돌면 총 a만큼이동해서 시작점에 도달. 

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
