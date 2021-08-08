# Time : O(N+K), Space: O(N)

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a = []
        for c in s:
            a.append(str(ord(c) - ord('a') + 1))
        ans = int("".join(a))
        for _ in range(k):
            s = 0
            while ans > 0:
                ans, d = divmod(ans, 10)
                s += d
            ans = s
        return ans
