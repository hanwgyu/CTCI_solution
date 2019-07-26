from collections import Counter
# Heuristic. 증명안해도되나?


# Solution 2
# 각 Task의 갯수를 세고, cooling중이지 않고 남은 갯수가 가장 많은 Task 순서대로 실행.
# n intervals를 단위로 한번에 실행한 후 sorting.
# (갯수가 줄어들은 task는 sorting후에도 항상 n intervals 이상의 실행간격을 보장)
# TimeComplexity : O(Total Intervals), SpaceComplexity : O(1)
class Solution(object):
    def leastInterval_2(self, tasks, n):
        remain, total_intervals = [0 for _ in range(26)], 0
        for task in tasks:
            remain[ord(task) - ord('A')] += 1
        
	remain.sort(reverse=True)
	while remain[0] > 0:
	    for i in range(n+1):
	        if remain[0] == 0:
	            break
	        if i < 26 and remain[i] > 0:
	            remain[i] -= 1
	            total_intervals += 1
	    remain.sort(reverse=True)

        return total_intervals

# Solution 1
# 각 Task의 갯수를 세고, cooling중이지 않고 남은 갯수가 가장 많은 Task 순서대로 실행.
# 매 interval마다 sorting. (Time Limit Exceeded)
# TimeComplexity : O(Total Intervals), SpaceComplexity : O(1)
    def leastInterval_1(self, tasks, n):
        task_num, total_intervals, cooling_intervals = Counter(tasks), 0, [0 for _ in range(26)]
        while sum(task_num.values()) > 0:
            # decrease cooling interval
            for i in range(len(cooling_intervals)):
                cooling_intervals[i] -= 1
            #Process Task
            tasks = [ i[0] for i in task_num.most_common()]
            for task in tasks:
                idx = ord(task)-ord('A')
                if cooling_intervals[idx] <= 0 and task_num[task] > 0:
                    cooling_intervals[idx] = n+1
                    task_num[task] -= 1
                    break
                total_intervals += 1
        return total_intervals

