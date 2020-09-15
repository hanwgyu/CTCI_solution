# Solution
# Time: O(N), Space: O(N)


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            q, r = divmod(len(s), i)
            if r == 0 and s[:i] * q == s:
                return True
        return False
