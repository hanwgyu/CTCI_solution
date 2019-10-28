#MergeSort 구현.
# Time : O(NlogN), Space : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def mergeSort(front: ListNode, n: int):
            if n == 1:
                return front
            mid = front
            for _ in range(n//2-1): 
                mid = mid.next
            # 두 리스트를 분리.
            temp = mid.next
            mid.next = None
            mid = temp
            
            node1 = mergeSort(front, n//2)
            node2 = mergeSort(mid, n - n//2)
            
            head = ListNode(0)
            cur = head
            while node1 and node2:
                if node1.val < node2.val:
                    cur.next, node1 = node1, node1.next
                else:
                    cur.next, node2 = node2, node2.next
                cur = cur.next
            while node1:
                cur.next, node1 = node1, node1.next
                cur = cur.next
            while node2:
                cur.next, node2 = node2, node2.next
                cur = cur.next
            return head.next
            
        if not head:
            return None
        node, n = head, 0
        while node:
            node, n = node.next, n+1
    
        return mergeSort(head, n)
