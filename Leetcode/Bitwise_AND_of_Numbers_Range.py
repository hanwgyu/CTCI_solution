#Time : O(1), Space : O(1)

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        cnt = 0
        while m != n:
            m, n, cnt = m >> 1, n >> 1, cnt + 1
        return m << cnt
