# Solution 1 : DP.
# Time : O(MN^2), Space : O(MN)
# Leetcode 테스트 결과 시간초과

# Solution 2 : Binary Search. Briiiiilliant!!!
# Binary Search로 Valid(m개로 쪼갠 Subarray들의 합보다 큼) 한 가장 작은 값을 구하면 그값은 항상 Subarray의 합으로 표현할 수 있다!
# Time: O(Nlog(sum(nums)-m)), Space : O(1)


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def valid(s: int, m: int) -> bool:
            """
            m개로 쪼갠 array들의 각각의 합이 s보다 작은지 체크
            """
            cur = 0
            for c in nums:
                if cur+c > s:
                    m -= 1
                    cur = 0
                cur += c
            return m >= 1

        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l+r)//2
            if valid(mid, m):
                r = mid - 1
            else:
                l = mid + 1
        return l

    def splitArray_1(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [
            [float("inf") for _ in range(min(i, m) + 1)] for i in range(n + 1)
        ]

        s = 0
        for i in range(1, n + 1):
            s += nums[i - 1]
            dp[i][1] = s

        for i in range(2, n + 1):
            for i_ in range(1, i):
                for j in range(2, min(m, i) + 1):
                    dp[i][j] = min(
                        dp[i][j],
                        max(dp[i_][j - 1], dp[i][1] - dp[i_][1])
                        if i_ >= j - 1
                        else float("inf"),
                    )

        return dp[n][m]
