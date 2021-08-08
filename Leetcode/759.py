# 어려워 보이지만, interval을 전체를 sorting하고 순차적으로 봐도 된다는 개념만 알아차리면 생각보다 쉽게 풀 수 있음.


# 풀이 1 : 모든 interval의 start, end 에 대해 sorted된 순서로 List를 만듬.
# 앞에서부터 iterate하면서 start, end 에 따라 active 값을 바꿔가면서 진행.
# active값이 0일때가 free time.

# 풀이 2: 1과 비슷하지만 좀더 간단한 풀이법
# https://leetcode.com/problems/employee-free-time/discuss/170551/Simple-Python-9-liner-beats-97-(with-explanation) 참고
# start time이 순차적으로 설정되어 있으므로, end time과 비교해 어떻게 되는지 케이스를 나누면됨
# case 1. s2 < e1, e2 < e1 : 이전 interval에 포함. 아무것도 안하고 넘기면됨
# case 2. s2 < e1, e1 < e2 : 이전 interval에 포함되지 않으나 free time은 없음. end time 업데이트.
# case 3. e1 < s2. e1~s2가 free time.


"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        itvs = sorted([i for s in schedule for i in s], key= lambda i : i.start)
        ans, pre = [], itvs[0]
        for itv in itvs[1:]:
            if itv.start <= pre.end and pre.end < itv.end:
                pre.end = itv.end
            elif pre.end < itv.start:
                ans.append(Interval(pre.end, itv.start))
                pre = itv
        return ans

    def employeeFreeTime_1(self, schedule: '[[Interval]]') -> '[Interval]':
        ts = []

        # 모든 interval의 start, end 에 대해 sorted된 순서로 List를 만듬.
        for intervals in schedule:
            for interval in intervals:
                ts.append((interval.start, 0))
                ts.append((interval.end, 1))
        ts.sort(key = lambda x: (x[0], x[1]))
        print(ts)

        active = 0
        start = 0
        free = False
        ans = []
        for (t, flag) in ts:
            if flag == 0: # start
                active += 1
            else:
                active -= 1
            if active == 0 and not free:
                free = True
                start = t
            elif active != 0 and free:
                free = False
                ans.append(Interval(start, t))
        return ans
