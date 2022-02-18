class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window 개선.
        """
        d = {}
        ans = i = 0
        for j, c in enumerate(s):
            if c in d and d[c] >= i:
                i = d[c] + 1
            d[c] = j
            ans = max(ans, j-i+1)
        return ans
    
    
    def lengthOfLongestSubstring1(self, s: str) -> int:
        """
        Sliding window
        """
        d = set()
        ans = i = 0
        for j, c in enumerate(s):
            while c in d:
                d.remove(s[i])
                i += 1
            d.add(c)
            ans = max(ans, j-i+1)
        return ans