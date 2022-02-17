# 문제 설명 : ( 나 ) 를 추가해 valid하게 만들것. 그 횟수를 구하라

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = 0
        res = 0
        for c in s:
            if c == "(":
                st += 1
            else:
                if st:
                    st -= 1
                else:
                    res += 1
        return res + st