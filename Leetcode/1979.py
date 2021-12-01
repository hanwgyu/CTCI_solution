# 유클리드 호제법
# https://namu.wiki/w/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C%20%ED%98%B8%EC%A0%9C%EB%B2%95
# Time : O(N+log(max(nums))^2), Space: O(1)

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = min(nums), max(nums)
        while a:
            a, b = b % a, a
        return b
