# 무조건 minimum energy- actual energy가 크고, minimum energy가 큰 것 부터 실행하면됨.
# Time : O(NlogN), Space: O(1)


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda e: (e[1] - e[0], e[1]), reverse=True)
        ans = a_sum = sum(a for a, m in tasks)
        for a, m in tasks:
            if a_sum < m:
                ans += m - a_sum
                a_sum = m
            a_sum -= a
        return ans
