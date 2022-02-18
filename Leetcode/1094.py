class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        prefix sum
        O(1000*log(1000)) / O(1000)
        """
        d = [0 for _ in range(1001)]
        for n, src, dst in trips:
            d[src] += n
            d[dst] -= n
        
        s = 0
        for e in d:
            s += e
            if s > capacity:
                return False
        return True
    
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        prefix sum
        O(1000*log(1000)) / O(1000)
        """
        d = defaultdict(int)
        for n, src, dst in trips:
            d[src] += n
            d[dst] -= n
        
        s = 0
        for i, n in sorted(d.items(), key=lambda e:e[0]):
            s += n
            if s > capacity:
                return False
        return True