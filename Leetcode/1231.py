# 문제 설명: sweetness 를 k+1 조각으로 나눠서 얻을 수 있는 argmax(min(sum)) 구하기

from typing import Tuple

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        """
        binary search로 최대한 줄여나아가면 마지막에는 항상 답이 된다.
        그래서 아래 풀이같이 굳이 나눌 필요 없다.
        """
        def solve(m: int, k: int) -> bool:
            s, n = 0, 0
            for sweet in sweetness:
                s += sweet
                if s >= m:
                    s, n = 0, n+1
            return True if n > k else False
    
        l, r, ans = 1, sum(sweetness), 0
        while l <= r:
            m = (l+r)//2
            if solve(m, k):
                l = m+1
                ans = m
            else:
                r = m-1
        return ans

    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        """
        possible 과 is_answer 로 binary search를 이동할 수 있는지와
        실제로 답이 되는지를 체크했음

        O(NlogS) / O(1)
        """
        def solve(m: int, k: int) -> Tuple[bool, bool]:
            is_answer, s, n = False, 0, 0
            for sweet in sweetness:
                s += sweet
                if s == m:
                    is_answer = True
                if s >= m:
                    s, n = 0, n+1
            return (True if n > k else False, is_answer if s != m else True)
    
        l, r, ans = 1, sum(sweetness), 0
        while l <= r:
            m = (l+r)//2
            possible, is_answer = solve(m, k)
            if possible:
                l = m+1
                # Only update when result is same as m
                if is_answer: ans = m
            else:
                r = m-1
        return ans