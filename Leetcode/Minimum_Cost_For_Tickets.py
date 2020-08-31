# Solution 1 : brute-force.
# Time : O(3^N), Space: O(N)
# Time Limit Exceeded

# Solution 2 : DP. binary search. 현재 day까지에 대한 Ticket의 최소 가격을 저장해나아감.
# Time : O(NlogN), Space : O(N)


class Solution:
    def mincostTickets_2(self, days: List[int], costs: List[int]) -> int:
        total_cost = [0]
        for i, day in enumerate(days):
            tmp = float("inf")
            for duration, cost in {
                1: costs[0],
                7: costs[1],
                30: costs[2],
            }.items():
                tmp = min(
                    tmp,
                    total_cost[bisect.bisect_right(days, day - duration, 0, i)]
                    + cost,
                )
            total_cost.append(tmp)
        return total_cost[len(days)]

    def mincostTickets_1(self, days: List[int], costs: List[int]) -> int:
        def dfs(day_idx: int, total_cost: int, ticket_validity: int) -> int:
            if day_idx == len(days):
                return total_cost
            day = days[day_idx]
            if day <= ticket_validity:
                return dfs(day_idx + 1, total_cost, ticket_validity)
            return min(
                dfs(day_idx + 1, total_cost + cost, day + duration - 1)
                for cost, duration in d.items()
            )

        d = {costs[0]: 1, costs[1]: 7, costs[2]: 30}
        return dfs(0, 0, -1)
