# Solution : stack에 넣어 리스트 변경함. Recursive하게 푸려했더니 next가 변경되어버려 문제가 생김.
# Time : O(N), Space : O(N)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def link(node: Node):
            if not node: return
            if self.last_node:
                self.last_node.next = node
                self.last_node.child = None
                node.prev = self.last_node
            self.last_node = node
        if not head: return
        self.last_node = None
        st = [head]
        while st:
            node = st.pop()
            if node.next: st.append(node.next)
            if node.child: st.append(node.child)
            link(node)
        return head
