# Time Complexity :O(N), Space Complexity : O(1)
class Solution(object):
    def reverseBetween(self, head, m, n):
        if (n - m) == 0:
            return head

        # Set (m-1) node
        if m == 1:
            before_node = ListNode(0)
            before_node.next = head
        else:
            before_node = head
            for _ in range(m - 2):
                before_node = before_node.next

        # Reverse (m) ~ (n) nodes
        front_node, change_node, back_node = (
            before_node.next.next,
            before_node.next,
            before_node,
        )
        for _ in range(n - m):
            back_node, change_node, front_node = (
                change_node,
                front_node,
                front_node.next,
            )
            change_node.next = back_node

        # Linking '(m-1) node to (n) node' and '(m) node to (n+1) node'
        before_node.next.next = front_node
        before_node.next = change_node

        # reset head if m == 1
        if m == 1:
            head = before_node.next

        return head
