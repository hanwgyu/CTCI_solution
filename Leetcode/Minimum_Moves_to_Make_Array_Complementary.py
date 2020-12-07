# brute-force. Time: O(N*limit)

# Solution : l,r 하나씩으로 만들 수 있는 최소, 최대 범위 값들과 합(l+r)들을 저장해놓고 case1 : (limit+1 -> 2) , case2 : (limit+1 -> 2*limit) 까지 순차적으로 계산.
# case 1: limit+1 -> 2. 최초 갯수 N/2에서 시작. (l+r)값과 동일할 경우 0번 바꿔도 되고, min(l,r)+1 보다 작아질 경우 2번 바꿔야함
# case 2: limit+1 -> 2*limit. 최초 갯수 N/2에서 시작. (l+r)값과 동일할 경우 0번 바꿔도 되고, max(l,r)+limit 보다 커질 경우 2번 바꿔야함
# Time : O(N+limit), Space : O(N)

from collections import defaultdict


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        ans = float("inf")
        sums, min_sums, max_sums = defaultdict(int), defaultdict(int), defaultdict(int)
        for i in range(N // 2):
            l, r = nums[i], nums[N - 1 - i]
            sums[l + r] += 1
            min_sums[min(l, r) + 1] += 1
            max_sums[max(l, r) + limit] += 1

        c = N // 2
        for sum in reversed(range(2, limit + 2)):
            ans = min(ans, c - sums[sum])
            c += min_sums[sum]
        c = N // 2
        for sum in range(limit + 1, 2 * limit + 1):
            ans = min(ans, c - sums[sum])
            c += max_sums[sum]
        return ans
