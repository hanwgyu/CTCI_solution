class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Sliding Window 1번 방법을 개선.
        i를 이동하면서 처음 조건을 만족할때까지 j를 이동하지 않음

        Time : O(S+T), Space : O(1)
        """
        d, n = Counter(t), len(t)
        ans, j = (0, float('inf')), 0
        for i in range(len(s)):
            n -= d[s[i]] > 0
            d[s[i]] -= 1
            if n == 0:
                while d[s[j]] < 0:
                    d[s[j]] += 1
                    j += 1
                if ans[1]-ans[0] > i-j:
                    ans = (j,i)
        return s[ans[0]:ans[1]+1] if ans[1] != float('inf') else ''
    def minWindow1(self, s: str, t: str) -> str:
        """
        Sliding Window
        """
        d = Counter(t)
        ans, j = (0, float('inf')), 0
        for i in range(len(s)):
            d[s[i]] -= 1
            if all(e<=0 for e in d.values()):
                while d[s[j]] < 0:
                    d[s[j]] += 1
                    j += 1
                if ans[1]-ans[0] > i-j:
                    ans = (j,i)
        return s[ans[0]:ans[1]+1] if ans[1] != float('inf') else ''