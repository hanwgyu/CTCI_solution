# Solution : 값들이 Integer이므로 곱하면 절대값은 커져감. 
# 왼쪽에서 오른쪽으로, 오른쪽에서 왼쪽으로 두번 보면서 누적된 곱의 최대값을 저장해나아가면 됨. 
# (-갯수가 홀수일경우에 한쪽 방향으로만 가면 최대값이 아님.)
# 0일때는 1로 reset 해줌.
# Time : O(N), Space: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        m = 1
        for n in nums:
            m *= n
            ans = max(ans, m)
            if n == 0: m = 1
        m = 1
        for n in reversed(nums):
            m *= n
            ans = max(ans, m)
            if n == 0: m = 1
        return ans
