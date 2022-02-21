# 문제 설명 : 리본들을 맘대로 잘라서 같은 길이의 k개 리본을 만들어야한다. 잘라서 남는 부분은 버려도된다.
# k개 리본의 최대 길이를 구하라.

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        """
        길이를 정해서 가능한지를 체크해야한다.
        0~max(ribbons)의 범위에서 binary search를 진행한다.
        
        """
        def solve(m: int, k: int) -> bool:
            n = 0
            for r in ribbons:
                n += r//m
                if n >= k:
                    return True
            return False
        
        l, r, ans = 1, max(ribbons), 0
        while l <= r:
            m = (l+r)//2
            if solve(m, k):
                l = m+1
                ans = m
            else:
                r = m-1
        return ans