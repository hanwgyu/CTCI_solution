# Time : O(logN), Space : O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            # pivot이 존재하지 않는 경우
            if nums[l] < nums[r]:
                if nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            # pivot이 m 뒤쪽에 존재하는 경우
            elif nums[l] < nums[m]:
                if nums[m] < target or target < nums[l]:
                    l = m+1
                else:
                    r = m-1
            # pivot이 m 앞쪽에 존재하는 경우
            elif nums[l] > nums[m]:
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1
            # l과 m이 같은 경우
            else:
                l = m+1
        return l if nums and nums[l] == target else -1
