# Solution 1 : 각 원소를 포함하는 increasing subsequence의 최대 갯수를 저장해나아감.
# Time : O(N^2), Space : O(N)

# Solution 2 : Binary Search 이용해, 입력 리스트의 왼쪽부터 확인하면서 새로운 sorted array를 만들어감.
# array내 숫자보다 큰 값이 올경우 원소를 추가하고, 그렇지 않을경우 적당한 위치에 업데이트함.
# 이 방법을 이용해서 만든 array는 가능한 LIS리스트는 아님. LIS 리스트를 구할수 있는 방법이 있나 확인필요.
# Time : O(NlogN), Space : O(N)
# https://codedoc.tistory.com/414

from bisect import bisect_left


class Solution:
    def lengthOfLIS_2(self, nums: List[int]) -> int:
        a = []
        for n in nums:
            pos = bisect_left(a, n)
            if pos == len(a):
                a.append(n)
            else:
                a[pos] = n
        return len(a)

    def lengthOfLIS_1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        dp = [1] * N
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
