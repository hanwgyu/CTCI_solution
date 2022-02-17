"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor_1(self, p: 'Node', q: 'Node') -> 'Node':
        """
        방문한 노드를 기록
        
        O(H) / O(H)
        """
        visited = set()
        while p:
            visited.add(p)
            p = p.parent
        while q:
            if q in visited:
                return q
            q = q.parent
        return None
    
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Cycle 찾듯이 반복하면, LCA에서 겹치게됨. LCA보다 위에서 겹치는 경우는 없다.
        
        O(H) / O(1)
        """
        n1, n2 = p, q
        while n1 != n2:
            n1 = n1.parent if n1.parent else p
            n2 = n2.parent if n2.parent else q
        return n1