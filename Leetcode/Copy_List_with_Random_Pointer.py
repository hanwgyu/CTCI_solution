# Solution : 1) Copy node from head to tail. Set 'random' of new copy node as 'random' of origin node. Then set 'random' of origin node as new copy node.
# 2) Change 'random' of copy node as 'random' of origin node in same index
# Time : O(N), Space : O(N)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        copy = dummy = Node(0, None, None)
        origin = head
        while origin:
            copy.next = Node(origin.val, origin.next, origin.random)
            origin.random = copy.next
            copy, origin = copy.next, origin.next
        copy = dummy
        while copy:
            if copy.random:
                copy.random = copy.random.random
            copy = copy.next
        return dummy.next
