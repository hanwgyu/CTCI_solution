class Solution:
    def maxEvents(self, A: List[List[int]]) -> int:
        """
        starttime 기준으로 greedy하게 sorting후 앞에서부터 선택?
        현재 day에서 가능한 event 중에서 endDay가 가장 작은 순서대로 리턴
        """
        A.sort(reverse=True)
        ends = []
        ans = start = 0
        while A or ends:
            # ends가 없으면 day를 jump가능.
            if not ends:
                day = A[-1][0]
            # day 가 start 이후에 포함되면 end를 heap 에 추가
            while A and A[-1][0] <= day:
                heapq.heappush(ends, A.pop()[1])
            # day 가 end를 지나섰으면 모두 pop.
            while ends and ends[0] < day:
                heapq.heappop(ends)
            # day 하나당 하나씩 event를 처리가능. 그다음 day로 이동
            if ends:
                heapq.heappop(ends)
                day += 1
                ans += 1
        return ans
