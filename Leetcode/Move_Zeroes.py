# Time : O(N), Space : O(1)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, pos = 0, 0  # pos는 0이 위치하는 가장 앞 idx를 가리킴

        while i < len(nums):
            if nums[i] != 0:
                if pos < i:
                    nums[i], nums[pos] = 0, nums[i]
                pos += 1
            i += 1
