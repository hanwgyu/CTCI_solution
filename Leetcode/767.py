class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        갯수가 많은 순서대로 출력하면 됨.
        Priority Queue
        
        O(NlogN) / O(N)
        """
        l = []
        d = Counter(s)
        for c, n in d.items():
            heapq.heappush(l, (-n, c))
        ans = []
        while l:
            n1, c1 = heapq.heappop(l)
            n1 = -n1
            ans.append(c1)
            if not l and n1 != 1:
                return ''
            if l:
                n2, c2 = heapq.heappop(l)
                n2 = -n2
                ans.append(c2)
                if n2 != 1: heapq.heappush(l, (-n2+1, c2))
            if n1 != 1: heapq.heappush(l, (-n1+1, c1))
        return ''.join(ans)
