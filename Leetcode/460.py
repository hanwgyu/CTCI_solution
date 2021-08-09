# 어려운 점은 put할때 LRU를 O(1)만에 알아내야한다는점. heap으로도 안됨.

# 풀이 1 : Deque + hash.
# Hash에 (값, count, deque내 idx)를 저장. hash로 get을 O(1)에 하고, Deque로 count를 오름 차순으로 정렬하여 관리하고, 가장 앞에 있는 원소를 pop.
# Time limit exceeded. 같은 값일때 옮기는 맨앞으로 로직이 비용이 많이드나?

# 풀이 2 : frequency마다 linked list를 따로 관리함.
# https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list 참고.

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DoubleLinkedList:
    """
    모두 O(1) 연산
    """
    def __init__(self):
        self.start = Node(None, None) # Dummy Node
        self.start.next = self.start.prev = self.start
        self.size = 0

    def __len__(self):
        # not DoubleLinkedList 조건을 판단하기 위해 사용
        return self.size

    def append(self, node: Node):
        node.next = self.start.next
        self.start.next.prev = node
        node.prev = self.start
        self.start.next = node
        self.size += 1

    def pop(self, node: Node = None):
        if self.size == 0:
            return

        if not node:
            node = self.start.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.freq = defaultdict(DoubleLinkedList)
        self.minfreq = 0
        self.nodes = {} #key : key, value : Node

    def _update(self, node: Node):
        """
        freq를 1 증가시켜서 저장.
        """
        freq = node.freq
        self.freq[freq].pop(node)
        if self.minfreq == freq and not self.freq[freq]:
            self.minfreq += 1
        node.freq += 1
        self.freq[freq+1].append(node)


    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.nodes:
            node = self.nodes[key]
            self._update(node)
            node.val = value
        else:
            if len(self.nodes) == self.cap:
                #delete LFU
                node = self.freq[self.minfreq].pop()
                del self.nodes[node.key]
            # Add new element
            node = Node(key, value)
            self.nodes[key] = node
            self.freq[1].append(node)
            self.minfreq = 1


class LFUCache1:

    def __init__(self, capacity: int):
        self.q = deque()
        self.d = {}
        self.cap = capacity

    def update_queue(self, key: int):
        """
        현재 dict 내 값에 따라 queue 내 key 위치를 업데이트 진행. (같은 count값들 중에서 가장 앞으로 옮김)
        """
        value, cnt, idx = self.d[key]
        for i in reversed(range(idx)):
            pre_key = self.q[i]
            pre_value, pre_cnt, _ = self.d[pre_key]
            if pre_cnt <= cnt:
                #swap queue
                self.q[i], self.q[i+1] =  self.q[i+1], self.q[i]
                # change dict
                self.d[key] = [value, cnt, i]
                self.d[pre_key] = [pre_value, pre_cnt, i+1]
            else:
                break

    def get(self, key: int) -> int:
        if key in self.d:
            self.d[key][1] += 1
            self.update_queue(key)
            return self.d[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.d:
            self.d[key] = [value, self.d[key][1]+1, self.d[key][2]]
        else:
            if len(self.d) == self.cap:
                #delete LRU
                k = self.q.pop()
                del self.d[k]
            # Add new element
            self.q.append(key)
            self.d[key] = [value, 1, len(self.q)-1]
        self.update_queue(key)



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
