# Time : O((N+K)logN), Space : O(N)

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        a = []
        for p in piles:
            heapq.heappush(a, -p)
        for _ in range(k):
            e = heapq.heappop(a)
            heapq.heappush(a, e//2)
        return -sum(a)
