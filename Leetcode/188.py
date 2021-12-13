# REMIND

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        최종 profit은 이런 형태. (ek-sk) + (ek-1 - sk-1) + ... + (e1 - s1)
        profits[i] = (ei - si) + ... + (e1 - s1) = ei - costs[i]
        costs[i] = si - ((ei-1 - si-1) + ... + (e1 - s1)) = si - profits[i]
        """
        costs = [0]+([float('inf')] * k)
        profits = [0] * (k+1)
        for p in prices:
            for i in range(1, k+1):
                costs[i] = min(costs[i], p - profits[i-1])
                profits[i] = max(profits[i], p - costs[i])
        return profits[-1]