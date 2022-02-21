# 문제 설명 : weights를 days 갯수 이하의 subarray들로 구성. subarray들의 합이 최소가 되게끔 구성.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        특정 합에 대해 모든 경우를 체크. 
        합을 바꿔가면서 체크할때 binary search로 효율적으로 체크함.
        
        O(Nlog(S)) / O(1) # S:sum(weights)
        """
        def solve(m: int) -> bool:
            s, n = 0, 1
            for w in weights:
                if w > m:
                    return False
                s += w
                if s > m:
                    s, n = w, n+1
                if n > days:
                    return False
            return True
        
        ans = 0
        l, r = 0, sum(weights)
        while l <= r:
            m = (l+r)//2
            if solve(m):
                r = m-1
                ans = m
            else:
                l = m+1
        return ans