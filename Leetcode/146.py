class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.d:
            n = self.d[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self._remove(self.d[key])
            del self.d[key]
        if len(self.d) == self.capacity:
            del self.d[self.head.next.key]
            self._remove(self.head.next)
        n = Node(key, value)
        self._add(n)
        self.d[key] = n
        
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        node.prev = p
        self.tail.prev = node