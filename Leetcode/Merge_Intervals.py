# Solution : left 값에 대해 Sort. 그 이후, 각 원소에 대해 left값과 이전 노드들의 right 최대값을 비교해 겹치는 부분이 있으면 right값을 업데이트하고,
# 겹치는 부분이 없으면 결과값에 추가.

# Time : O(NlogN), Space : O(N)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        
        intervals.sort(key=lambda e:e[0])
        ans, l, r = [], intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if r >= intervals[i][0]:
                r = max(r, intervals[i][1])
            else:
                ans.append([l, r])
                l, r = intervals[i][0], intervals[i][1]
        ans.append([l, r])
        return ans
            
