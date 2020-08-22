# Solution : 뒤의 자리부터 Permutation의 맨 끝인지를 확인 (이전 자리까지의 가장 큰 숫자와 현재 자리의 숫자를 비교)
# Permutation 맨끝이 아닌 시점을 기준으로 자기보다 큰 수가 위치하는 자리와 스왑하고
# 이전 자리들은 오름 차순으로 정렬시킴. (내림차순 -> 오름차순으로)
# Time : O(N), Space: O(1)


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N, i, m = len(nums), len(nums) - 1, float("-inf")
        while i >= 0 and nums[i] >= m:
            m, i = max(m, nums[i]), i - 1
        # find bigger element location and swap with target
        if i >= 0:
            j = i + 1
            while j < N and nums[j] > nums[i]:
                j = j + 1
            nums[i], nums[j - 1] = nums[j - 1], nums[i]
        # ordering
        i, j = i + 1, N - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
