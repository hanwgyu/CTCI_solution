# Solution : DP.
# Time : O(len(s)*len(p)), Space: O(len(s)*len(p))

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[len(s)][len(p)] = True
        
        if len(p) == 0:
            return dp[0][0]
        elif p[len(p)-1] == '*':
            dp[len(s)][len(p)-2] = True
        
        for j in reversed(range(len(p))):
            if p[j] == '*':
                continue
            elif j+1 < len(p) and p[j+1] != '*':
                break
            elif j == len(p)-1 and p[j] != '*':
                break
            elif j+1 < len(p) and p[j+1] == '*':
                dp[len(s)][j] = True
            
        for j in reversed(range(len(p))):
            for i in reversed(range(len(s))):
                if p[j] == '.':
                    if j+1 < len(p) and p[j+1] == '*':
                        for k in range(i, len(s)+1):
                            if dp[k][j+2]:
                                dp[i][j] = True
                                break
                    else:
                        dp[i][j] = dp[i+1][j+1]
                elif p[j] == '*':
                    continue
                elif j+1 < len(p) and p[j+1] == '*':
                    if p[j] != s[i]:
                        dp[i][j] = dp[i][j+2]
                    else:
                        for k in range(i, len(s)+1):
                            if dp[k][j+2]:
                                dp[i][j] = True
                                break
                            if k < len(s) and s[k] != p[j]:
                                break
                elif p[j] == s[i]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    continue
        return dp[0][0]   
