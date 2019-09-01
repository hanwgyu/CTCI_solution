#Time : O(log10(X)), Space : O(1)

class Solution:
    def reverse(self, x: int) -> int:
        ans, neg = 0, False
        if x < 0:
            neg, x = True, -x
        while x > 0:
            ans, x = ans*10 + x%10, x//10
        ans = -ans if neg else ans
        return ans if -2**31 < ans < 2**31 - 1 else 0
