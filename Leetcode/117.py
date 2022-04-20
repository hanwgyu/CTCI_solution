class Solution:
    
    """
    bfs
    1. 큐에 level를 같이 저장
    2. level를 저장하지 않고, rightmost 노드일때 queue의 size를 측정해 그 다음 rightmost 노드를 알아낸다.
    """
    
    def connect(self, root: 'Node') -> 'Node':
        """
        현재 레벨의 next로 이동하면서 다음 레벨의 child 들을 연결한다.
        
        O(N) / O(1)
        """
        node = root
        while node:
            # same level
            prev = dummy = Node(0)
            while node:
                if node.left:
                    if prev:
                        prev.next = node.left
                    prev = node.left
                if node.right:
                    if prev:
                        prev.next = node.right
                    prev = node.right
                node = node.next
            # next level
            node = dummy.next
        return root
