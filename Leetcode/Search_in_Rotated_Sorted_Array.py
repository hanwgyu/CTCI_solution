# Time : O(logN), Space : O(1)
# 범위 설정하는 것이 상당히 까다로움. 여러번 시행착오를 거쳐 해답을 찾아냈음.

# Solution 3 : 일반 binary search하는 것처럼 동작시키기 위해 target과 nums[m]값이 
# 위치하는 수열이 다른 경우, inf, -inf값으로 설정해 search를 동작시킨다.

class Solution:
    def search_3(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1        
        while l <= r:
            m = (l+r)//2
            num = nums[m] if (target < nums[0]) == (nums[m] < nums[0]) else (float('-inf') if target < nums[0] else float('inf'))
            if num < target:
                l = m + 1
            elif num > target:
                r = m - 1
            else:
                return m
        return -1

    
    def search_2(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target: return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]: r = m - 1
                else: l = m + 1
            else:
                if nums[m] < target <= nums[r]: l = m + 1
                else: r = m - 1
        return -1
                
    
    def search_1(self, nums: List[int], target: int) -> int:
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
