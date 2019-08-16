# Time : O(N), Space : O(1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
