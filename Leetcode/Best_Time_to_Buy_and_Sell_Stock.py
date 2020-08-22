# Time : O(N), Space: O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, min_price = 0, float("inf")
        for price in prices:
            ans = max(ans, price - min_price)
            min_price = min(min_price, price)
        return ans
