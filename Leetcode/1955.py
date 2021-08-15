# 고민 1: DP. 1) 0,1로 끝났을때, 2를 새롭게 추가하거나, 1을 추가한 케이스를 계산 2)2로 끝났을때, 2가 추가되던지 아니던지
# TIme : O(N), Space : O(1)

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp0, dp1, dp2 = 0, 0, 0

        for num in nums:
            if num == 0:
                dp0 = dp0 * 2 + 1
            elif num == 1:
                dp1 = dp0 + dp1 * 2
            elif num == 2:
                dp2 = dp1 + dp2 * 2
        return dp2 % (pow(10, 9) + 7)
