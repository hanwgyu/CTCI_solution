# Solution 1 : DP. 글자수를 하나씩 늘려가며 두 글자 전에 저장해놓은 결과값과 맨앞, 맨뒤 글자가 똑같은지 여부를 이용해 현재 결과를 계산.
# Time : O(L^2), Space : O(L^2)

# Solution 2 : DP. 공간복잡도 줄임.
# Time : O(L^2), Space : O(L)


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        brute-force : O(N^3) / O(1)
        
        중심지를 기준으로 확장. O(N^2) / O(1)
        """
        ans = 0
        N = len(s)
        for i in range(N):
            j = 0
            # odd
            while 0<=i-j<N and 0<=i+j<N and s[i+j] == s[i-j]:
                ans, j = ans+1, j+1
            j = 0
            # odd
            while 0<=i-j<N and 0<=i+j+1<N and s[i+j+1] == s[i-j]:
                ans, j = ans+1, j+1
        return ans

class Solution:
    def countSubstrings_2(self, s: str) -> int:
        L, ans = len(s), 0
        dp1 = [True for _ in range(L + 1)]
        dp2 = [True for _ in range(L + 1)]
        ans += L

        for l in range(L - 1):
            for i in range(1, L - l):
                if dp1[i] and s[i - 1] == s[i + l]:
                    dp1[i - 1], ans = True, ans + 1
                else:
                    dp1[i - 1] = False
            dp1, dp2 = dp2, dp1
        return ans

    def countSubstrings_1(self, s: str) -> int:
        L, ans = len(s), 0
        dp = [[False for _ in range(L + 1)] for _ in range(L)]
        for i in range(L):
            dp[i][i], dp[i][i + 1] = True, True
            ans += 1

        for l in range(L - 1):
            for i in range(1, L - l):
                if dp[i][i + l] and s[i - 1] == s[i + l]:
                    dp[i - 1][i + l + 1], ans = True, ans + 1
        return ans
