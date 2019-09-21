#Time : O(N), Space : O(1)

class Solution:
    def numDecodings(self, s: str) -> int:
        def canEncode(num : str) -> bool:
            if num[0] == '0': return False
            return True if 1<= int(num) and int(num) <= 26 else False
        
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1 if canEncode(s[0]) else 0
        dp_1, dp_2  =  (1 if canEncode(s[0]) and canEncode(s[1]) else 0) + (1 if canEncode(s[0:2]) else 0), 1 if canEncode(s[0]) else 0
        for i in range(2, len(s)):
            dp_1, dp_2  = (dp_1 if canEncode(s[i]) else 0) + (dp_2 if canEncode(s[i-1:i+1]) else 0), dp_1
        return dp_1
            
