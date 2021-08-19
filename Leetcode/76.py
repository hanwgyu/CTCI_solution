# 고민 1: 모든 character를 포함할때까지 right pointer를 증가시키고, 모든 character가 포함되면 left pointer를 증가시킴.
# Time : O(S+T), Space : O(S+T)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, n = collections.Counter(t), len(t)
        l = 0
        ans_l, ans_r = 0, 0
        for r, c in enumerate(s, 1):
            n -= need[c] > 0
            need[c] -= 1
            if n == 0:
                # s에 없는 문자들은 항상 마이너스여서, while문 조건에 항상 속하게 된다.
                while l < r and need[s[l]] < 0:
                    need[s[l]] += 1
                    l += 1
                if ans_r == 0 or ans_r - ans_l > r-l:
                    ans_l, ans_r = l, r
        return s[ans_l:ans_r]
