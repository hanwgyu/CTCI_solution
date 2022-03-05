class Solution:
    def minCut(self, s: str) -> int:
        """
        DP.
        Palindrome을 홀수, 짝수 갯수로 나눠서 확장시켜나가면서 DP 계산
        
        O(N^2) / O(N)
        """
        N = len(s)
        dp = [i for i in range(-1, N)]
        for i in range(N):
            ro, re = 0, 0
            # odd palindrome
            while i-ro >= 0 and i+ro < N and s[i-ro] == s[i+ro]:
                dp[i+ro+1] = min(dp[i+ro+1], dp[i-ro]+1)
                ro += 1
            # even palindrome
            while i-re >= 0 and i+re+1 < N and s[i-re] == s[i+re+1]:
                dp[i+re+2] = min(dp[i+re+2], dp[i-re]+1)
                re += 1
        return dp[-1]
        
    
    def minCut2(self, s: str) -> int:
        """
        DP
        
        O(N^3) / O(N)
        """
        dp = [0]
        N = len(s)
        for i in range(N):
            dp.append(min(dp[j]+1 for j in range(i+1) if s[j:i+1] == s[j:i+1][::-1]))
        return dp[-1]-1
        
    
    def minCut1(self, s: str) -> int:
        """
        brute-force
        """
        def solve(s: str) -> int:
            if s == '':
                return 0
            N = len(s)
            res = float('inf')
            for i in range(1, N+1):
                s1 = s[:i]
                if s1 == s1[::-1]:
                    res = min(res, 1+solve(s[i:]))
            for i in reversed(range(N)):
                s1 = s[i:]
                if s1 == s1[::-1]:
                    res = min(res, 1+solve(s[:i]))
            return res
        return solve(s)-1