# Time Complexity : O(N), Space Complexity : O(1)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        node_a, node_b = headA, headB
        len_a, len_b = 0, 0

        while node_a:
            len_a += 1
            node_a = node_a.next
        while node_b:
            len_b += 1
            node_b = node_b.next

        node_a, node_b = headA, headB
        if len_a > len_b:
            for _ in range(len_a - len_b):
                node_a = node_a.next
        else:
            for _ in range(len_b - len_a):
                node_b = node_b.next

        while node_a != node_b:
            node_a = node_a.next
            node_b = node_b.next

        return node_a
