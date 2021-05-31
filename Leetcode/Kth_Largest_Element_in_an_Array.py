import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSort(l, r):
            if r-l <= 0:
                return
            pivot = random.randint(l, r)
            pos = partition(l, r, pivot)
            quickSort(l, pos-1)
            quickSort(pos+1, r)
        def partition(l, r, pivot):
            nums[r], nums[pivot] = nums[pivot], nums[r]
            pivot = r
            r = r-1
            while l <= r:
                # desc order로 sorting.
                if nums[l] >= nums[pivot]:
                    l += 1
                elif nums[pivot] >= nums[r]:
                    r -= 1
                else:
                    nums[l], nums[r] = nums[r], nums[l]
            print(nums, l, r, pivot)
            nums[l], nums[pivot] = nums[pivot], nums[l]   
            return l
            
        l, r = 0, len(nums) - 1
        while True:
            pivot = random.randint(l, r)
            pos = partition(l, r, pivot)
            if pos < k-1:
                l = pos+1
            elif pos > k-1:
                r = pos-1
            else:
                return nums[k-1]

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
