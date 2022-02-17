import heapq

class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        O(NlogN) / O(N)
        """
        d = Counter(words)
        return [k for k, _ in sorted(d.items(), key=lambda e: (-e[1],e[0]))[:k]]
    
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        BST의 크기를 k로 유지해나아감.
        """
        d = Counter(words)
        l = []
        for word, cnt in d.items():
            node = Node(word, cnt)
            heapq.heappush(l, node)
            if len(l) > k:
                heapq.heappop(l)
        
        res = []
        while l:
            res.append(heapq.heappop(l).word)
        return res[::-1]