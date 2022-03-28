# Solution : 두 리스트의 길이를 맞춰준 후 (짧은 리스트는 앞쪽에 0의 값을 가진 ListNode를 추가), Recursive하게 구현하여 다음 노드의 계산 결과값을 이용.
# Time : O(max(N,M)), Space : O(max(N,M)) (Recursive stack)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        그냥 계산해서 새로운 리스트를 생성
        """
        s1, s2 = 0, 0
        p1, p2 = l1, l2
        while p1:
            s1 = s1* 10 + p1.val
            p1 = p1.next
        while p2:
            s2 = s2* 10 + p2.val
            p2 = p2.next
        p = head = ListNode()
        for c in str(s1+s2):
            p.next = ListNode(int(c))
            p = p.next
        return head.next
        
            

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def expandListFront(node: ListNode, length: int, val: int) -> ListNode:
            for _ in range(length):
                temp = ListNode(val)
                temp.next = node
                node = temp
            return node

        # Carry를 리턴하고, cur1 링크드리스트에 결과값을 추가.
        def addCurrentNode(cur1: ListNode, cur2: ListNode) -> int:
            carry = 0
            if cur1.next and cur2.next:
                carry = addCurrentNode(cur1.next, cur2.next)
            s = cur1.val + cur2.val + carry
            cur1.val = s % 10
            return s // 10

        n1, cur1, n2, cur2 = 0, l1, 0, l2
        while cur1:
            cur1, n1 = cur1.next, n1 + 1
        while cur2:
            cur2, n2 = cur2.next, n2 + 1
        if n1 < n2:
            l1 = expandListFront(l1, n2 - n1, 0)
        else:
            l2 = expandListFront(l2, n1 - n2, 0)

        carry = addCurrentNode(l1, l2)
        if carry == 1:
            l1 = expandListFront(l1, 1, 1)
        return l1
