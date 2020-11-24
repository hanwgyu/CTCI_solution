# bruteforce. Time:O(N^2), Space: O(N^2)

# 각 양쪽에서의 합을 set에 저장하고 (모든 값이 양수이므로 점점 커지는 다른 값들이 저장됨), diff를 찾음.
# Time:O(N), Space: O(N)


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        d = {0: 0}
        s = 0
        for i, num in enumerate(nums):
            s += num
            if s > x:
                break
            d[s] = i + 1
        s = 0
        ans = float("inf") if x not in d else d[x]
        for j in reversed(range(len(nums))):
            s += nums[j]
            if s > x:
                break
            if x - s in d and d[x - s] < j:
                ans = min(ans, d[x - s] + len(nums) - j)
        return -1 if ans == float("inf") else ans
