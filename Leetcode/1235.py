# 고민 1 : DP. startTime 이 작은 순서대로 최대 profif을 저장해나아감.
#  startTime보다 작은 endTime 값들 중에서 가장 profit 합이 큰 것을 기준으로 dp를 계산해나아가야함.
# endTime을 sort된 순서로 저장하여 binary Search가 가능하게함.
# profit을 기존 값들에 대한 max값을 업데이트해나아감.
# 기존 값들을 업데이트하는 비용이 많이듬. (현재 포인트 이후 값들을 모두 업데이트 해야함 )

# 고민 2 : DP + binary search. endTIme이 작은 순서대로 최대 profif을 저장해나아감.
# endTime을 기준으로 sorting을 하고, 그 array에서 binary Search를 진행할 수 있음
# 또한 최대 profit을 업데이트 할때 기존 값들 중에서 가장 큰 값과 현재 값의 max를 저장해나아가면됨. (endTime이 오름 차순이기 때문에.)
# Time : O(NlogN), Space: O(N)

# 고민 3 : DP + heap. startTime 이 작은 순서대로 진행해  heap에 end time이 작은 순서대로 최대 profif을 저장해나아감.
# 현재 startTime보다 작은 endTime은 모두 이미 처리가 된 상태.
# 현재 startTime에 대해 endTime이 가장 가까워질때까지 pop하면서 최대 profit을 구함.

from collections import defaultdict
import bisect
import heapq

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        heap = []
        time = []
        for i in range(len(startTime)):
            time.append((startTime[i], endTime[i], profit[i]))
        time.sort(key = lambda x: x[0])
        ans = 0
        profit = 0 # 이부분이 중요함. (startTime이 오름 차순이므로, 이전 endTime들중 최대 profit을 항상 저장할 수 있음)
        for s, e, p in time:
            while heap and heap[0][0] <= s:
                _, p_ = heapq.heappop(heap)
                profit = max(profit, p_)
            heapq.heappush(heap, (e, profit+p))
            ans = max(ans, profit+p)
        return ans

    def jobScheduling_2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = [0]
        time = []
        for i in range(len(startTime)):
            time.append((startTime[i], endTime[i], profit[i]))
        time.sort(key = lambda x: x[1])
        endtime = [0]+[e for s, e, p in time]
        for s, e, p in time:
            i = bisect.bisect_right(endtime, s)
            profit = dp[i-1]+p
            dp.append(max(dp[-1], profit))
        return dp[-1]
