# Solution 1: dfs
# Time : O(2^N), Space : O(N)

# Solution 2: Backtracking (dfs + memory)
# Time : O(N^2), Space : O(N^2)

# Solution 3: DP
# Time : O(N^2), Space : O(N^2)

# Solution 4: DP with less memory
# Time : O(N^2), Space : O(N)

class Solution:
    def longestPalindromeSubseq_4(self, s: str) -> int:
        N = len(s)
        dp = [1 for _ in range(N)] #use dp[i] for dp[i][i]
        for j in range(1, N): # end index
            pre = dp[j] #save dp[i+1][j-1] for index i (j == i+1)
            for i in reversed(range(j)): # start index
                tmp = dp[i] #save dp[i+1][j-1] for index i
                if s[i] == s[j]:
                    dp[i] = 2+pre if j-i > 1 else 2 
                else: 
                    dp[i] = max(dp[i], dp[i+1])
                pre = tmp
        return dp[0]
    
    def longestPalindromeSubseq_3(self, s: str) -> int:
        N = len(s)
        dp = [[0 for _ in range(N)] for _ in range(N)] # longest palindrome in s[i:j+1]
        for i in range(N): dp[i][i] = 1
        for j in range(1, N): # end index
            for i in reversed(range(j)): # start index
                dp[i][j] = 2+dp[i+1][j-1] if s[i] == s[j] else max(dp[i][j-1], dp[i+1][j]) 
        return dp[0][N-1]
                
    def longestPalindromeSubseq_2(self, s: str) -> int:
        def find(l: int, r: int, s: str) -> int:
            if (l,r) in d: return d[(l,r)]
            if l == r:  return 1
            elif l > r: return 0
            d[(l,r)] = 2+find(l+1,r-1,s) if s[l] == s[r] else max(find(l,r-1,s), find(l+1, r,s))
            return d[(l,r)]
        d = {}
        return find(0,len(s)-1,s)
                
    def longestPalindromeSubseq_1(self, s: str) -> int:
        def find(l: int, r: int, s: str) -> int:
            if l == r: return 1
            elif l > r: return 0
            return 2+find(l+1,r-1,s) if s[l] == s[r] else max(find(l,r-1,s), find(l+1, r,s))
        return find(0, len(s)-1, s)
