# LIS

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        a, ans = [], []
        for o in obstacles:
            i = bisect.bisect_right(a, o)
            if i == len(a):
                a.append(o)
            else:
                a[i] = o
            ans.append(i+1)
        return ans
