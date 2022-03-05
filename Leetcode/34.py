class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_left(nums: List[int], target: int) -> int:
            l, r = 0, len(nums)-1
            while l <= r:
                m = (l+r)//2
                if nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            return l
        
        def binary_search_right(nums: List[int], target: int) -> int:
            l, r = 0, len(nums)-1
            while l <= r:
                m = (l+r)//2
                if nums[m] <= target:
                    l = m+1
                else:
                    r = m-1
            return l
        
        #i, j = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
        i, j = binary_search_left(nums, target), binary_search_right(nums, target)
        return [i, j-1] if i != j else [-1, -1]