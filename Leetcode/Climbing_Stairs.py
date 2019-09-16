# Solution : DP. Time : O(N), Space : O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        step_2, step_1 = 1, 2
        for i in range(2, n):
            step_1, step_2 = step_2 + step_1, step_1
        return step_1
