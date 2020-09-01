# brute-force. Time : O(N^2)

# Solution : start point 들만 sorting해서, binary search.
# Time : O(NlogN), Space : O(N)

# start point, end point에 대한 array들을 sorting. 그 이후 두 array를 비교하면. O(N)

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_points, ret = [(e[0], i) for i, e in enumerate(intervals)], []
        start_points = sorted(start_points, key=lambda p: p[0])
        d = [e for e, _ in start_points]
        for _, end_point in intervals:
            i = bisect.bisect_left(d, end_point)
            ret.append(start_points[i][1] if i < len(start_points) else -1)
        return ret
