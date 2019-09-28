#Time : O(N), Space : O(1)

class Solution:
    # 진우님 솔루션, https://github.com/Curt-Park/algorithm_practice/blob/master/dp/decode_ways.py
    def numDecodings(self, s: str) -> int:
        """O(N) / O(1)"""
        two, a, b, c = 0, 1, 1, 0
        for ch in s:
            one = int(ch)
            two = two % 10 * 10 + one
            c += b if 1 <= one <= 9 else 0
            c += a if 10 <= two <= 26 else 0
            a, b, c = b, c, 0
        return b
    
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
            
