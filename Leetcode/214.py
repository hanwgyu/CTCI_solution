class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        s를 일단 거꾸로 뒤집고, 최대한 많이 겹칠 수 있게 만들어보기.
        겹치는 부분을 제외한 문자를 앞쪽에 거꾸로 추가하면됨.
        
        문자열 비교를 위해 rolling hash 쓰기.
        
        O(N) / O(1)
        """
        BASE, MOD = 26, 10**9+7 # N of lowercase alphabets : 25
        ans = 0
        front, back = 0, 0
        pow_base = 1
        for i, c  in enumerate(s):
            front = (front * BASE + ord(c) - ord('a')) % MOD
            back = (back + (ord(c) - ord('a')) * pow_base) % MOD
            pow_base *= BASE
            if front == back:
                # double check
                if s[:i+1] == s[:i+1][::-1]: 
                    ans = i+1
        return s[ans:][::-1]+s