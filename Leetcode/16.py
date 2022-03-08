class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Two pointer로 푼다.
        
        O(N^2) / O(1)
        """
        N, mindiff = len(nums), float('inf')
        nums.sort()
        for i in range(N-2):
            l, r = i+1, N-1
            while l < r:
                diff = target - (nums[i]+nums[l]+nums[r])
                mindiff = min(mindiff, diff, key=abs)
                if diff > 0:
                    l += 1
                elif diff < 0:
                    r -= 1
                else:
                    return target
        return target - mindiff  