# 모두 2로 나눈채로 시작 ('n//(n&-n)'으로 뒤쪽에 있는 연속된 0을 제거.)
# heap에 넣어서 가장 작은 값들부터 2배씩 증가시켜가면서 max값을 업데이트하고, 결과를 업데이트해나아감.
# heap에서 꺼낸 가장 작은 값을 더이상 업데이트 시킬 수 없으면 종료.
# Time : O(N*logN*logM), Space: O(N) (M : max(nums))

import heapq


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, [n // (n & -n), n])
        ans = float("inf")
        max_n = max(n for n, n0 in pq)
        while len(pq) == len(nums):
            n, n0 = heapq.heappop(pq)
            ans = min(ans, max_n - n)
            if n % 2 == 1 or n < n0:
                heapq.heappush(pq, [n * 2, n0])
                max_n = max(max_n, n * 2)
        return ans
