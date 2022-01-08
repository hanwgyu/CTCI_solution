# 문제 해설 : 앞뒤로 range 만큼을 물을 줄 수 있음. 모든 garden을 물을 주기 위한 최소 수도꼭지 갯수는?

# 1024번과 동일함

# O(NlogN) / O(N)

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        ranges = sorted([(i-r, i+r) for i, r in enumerate(ranges)])
        res, pivot, end = 0, float('-inf'), 0
        for i, j in ranges:
            if end >= n or i > end:
                break
            elif pivot < i:
                res, pivot = res + 1, end            
            end = max(end, j)
        return res if end >= n else -1