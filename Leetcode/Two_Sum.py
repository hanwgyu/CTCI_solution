# Sol 1 : BruteForce, Time : O(n^2), Space : O(1)
# Sol 2 : Using two pointer after sorting , Time : O(NlogN), Space : O(N)
# Sol 3 : Use Hash, Time : O(N), Space : O(N)

class Solution(object):
    def twoSum_3(self, nums, target):
        a = dict()
        for i in range(len(nums)):
            a[nums[i]] = i
        for j in range(len(nums)):
            i = a.get(target-nums[j])
            if i and i != j:
                return [i, j] 
        return []
    
    def twoSum_2(self, nums, target):
        a = [(nums[i], i) for i in range(len(nums))]
        a = sorted(a, key=lambda e : e[0])
        l, r = 0, len(nums) - 1
        while l < r:
            s = a[l][0] + a[r][0]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [a[l][1], a[r][1]]
        return []
        
