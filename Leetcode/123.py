# 고민 1: DP. 한번의 거래에 대한 값들을 저장. 한번 거래 이후 최소 값을 업데이트해나아감.
# Time : O(N^2), Space : O(N)

# 고민 2 : DP. 왼쪽, 오른쪽에서 최대값들을 저장함.
# Time : O(N), Space: O(N)

# 고민 3: one pass로.
# Time : O(N), Space: O(1)

# 어렵고.. 신기한 문제.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t1_profit, t2_cost, t2_profit = float('inf'), 0, float('inf'), 0
        for p in prices:
            t1_cost = min(t1_cost, p)
            t1_profit = max(t1_profit, p - t1_cost)
            t2_cost = min(t2_cost, p - t1_profit)
            t2_profit = max(t2_profit, p - t2_cost)
        return t2_profit

    def maxProfit_2(self, prices: List[int]) -> int:
        l_min, r_max = prices[0], prices[-1]
        L = len(prices)
        l_dp, r_dp = [0] * L, [0] * L
        for i in range(1, L):
            l_dp[i] = max(l_dp[i-1], prices[i] - l_min)
            r_dp[L-1-i] = max(r_dp[L-i], r_max - prices[L-1-i])
            l_min = min(l_min, prices[i])
            r_max = max(r_max, prices[L-1-i])
        ans = 0
        for i in range(L):
            ans = max(ans, l_dp[i] + r_dp[i])
        return ans



    def maxProfit_1(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        m = [float('inf')] * len(prices)
        m[0] = prices[0]
        ans = 0
        for i, p in enumerate(prices[1:], start=1):
            dp[i] = min((p-m[0]) for j in range(i))
            ans = max(ans, max((dp[j]+p-m[j]) for j in range(i)))
            for j in range(i+1):
                m[j] = min(m[j], p)
        return ans
