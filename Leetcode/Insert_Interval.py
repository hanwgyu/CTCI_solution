# Time : O(N), Space : O(N)


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ret = []
        i = -1
        for i, [x, y] in enumerate(intervals):
            if y < newInterval[0]:
                ret.append([x, y])
            elif newInterval[1] < x:
                i -= 1
                break
            else:
                newInterval[1] = max(y, newInterval[1])
                newInterval[0] = min(x, newInterval[0])
        return ret + [newInterval] + intervals[i + 1 :]
