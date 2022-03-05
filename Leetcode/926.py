class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp0, dp1 = 0, 0
        for c in s:
            if c == "0":
                dp1 = min(dp0+1, dp1+1)
            else:
                dp0, dp1 = dp0+1, min(dp0, dp1)
        return min(dp0, dp1)