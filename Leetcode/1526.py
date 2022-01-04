# DP 
# 값이 커질때만 결과를 증가시킴.
# REMIND: 값이 작아지는건 이전에 높았던 부분의 값과 동일하게 처리됨.

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = temp = 0
        for a in target:
            res += max(a-temp, 0)
            temp = a
        return res