class Solution:
    def maxEvents(self, A: List[List[int]]) -> int:
        """
        greedy하게 sorting후 앞에서부터 선택?
        현재 day에서 가능한 event 중에서 endDay가 가장 작은 순서대로 리턴
        """
        A.sort(reverse=True)
        ends = []
        ans = d = 0
        while A or ends:
            if not ends:
                d = A[-1][0]
            while A and A[-1][0] <= d:
                heapq.heappush(ends, A.pop()[1])
            while ends and ends[0] < d:
                heapq.heappop(ends)
            if ends:
                heapq.heappop(ends)
                d += 1
                ans += 1
        return ans

        