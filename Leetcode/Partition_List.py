# Time Complexity : O(N), Space Complexity : O(1)
class Solution(object):
    def partition(self, head, x):
        less_node, greater_node = ListNode(0), ListNode(0)
        less_head, greater_head = less_node, greater_node
        check_node = head

        while check_node:
            if check_node.val < x:
                less_node.next = check_node
                less_node = less_node.next
            else:
                greater_node.next = check_node
                greater_node = greater_node.next
            check_node = check_node.next

        greater_node.next = None
        less_node.next = greater_head.next

        return less_head.next
