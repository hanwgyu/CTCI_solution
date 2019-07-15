# Time Complexity : O(N), Space Complexity : O(N)
class Solution(object):
    def longestValidParentheses(self, s):
        total_length = len(s)
        
        sol = 0
        dp = [0] * total_length #dp[length]는 length위치에 있는 문자를 항상 포함하면서 만들수있는 최대 문자열 길이.
            
        for length in range(1, total_length):
            if s[length] == ')':
                if s[length - 1] == '(':
                    dp[length] = (dp[length-2] if length >= 2 else 0) + 2
                elif length - dp[length - 1] > 0 and s[length - 1 - dp[length - 1]] == '(':
                        dp[length] = dp[length - 1] + 2 + (dp[length - 2 - dp[length - 1]] if length >= 2 else 0)
                if sol < dp[length]:
                    sol = dp[length]
        return sol
            
        
