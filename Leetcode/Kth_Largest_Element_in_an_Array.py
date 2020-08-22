import random


class Solution(object):
    # Solution : Using quicksort
    # TimeComplexity : Avg O(N), SpaceComplexity : O(1)
    def findKthLargest(self, nums, k):
        def quickSort(l, r, pivot):
            nums[pivot], nums[r] = nums[r], nums[pivot]
            pivot, r = r, r - 1
            while l <= r:
                if nums[l] >= nums[pivot]:
                    l += 1
                elif nums[pivot] >= nums[r]:
                    r -= 1
                else:
                    nums[l], nums[r] = nums[r], nums[l]
            nums[l], nums[pivot] = nums[pivot], nums[l]
            return l

        l, r = 0, len(nums) - 1
        while True:
            pivot = random.randrange(l, r + 1)
            pos = quickSort(l, r, pivot)
            if k - 1 == pos:
                return nums[pos]
            elif k - 1 < pos:
                r = pos - 1
            else:
                l = pos + 1
