# Solution 0: Brute Force . Time : O(N^2) , Space : O(1)

# Solution 1: Use Hash. Save {sum(0...n) : n} into hash. 
# Diff of two elements are continuous subarrays ("sum(0...n) - sum(0..m) = sum(m...n) (if m<n)). 
# Time : Avg O(N), Space : O(N)


class Solution(object):
    def subarraySum_1(self, nums, k):
        a = {0:[-1]}
        ans, sum = 0, 0
        for n in range(len(nums)):
            sum += nums[n]
            if sum in a:
                a[sum].append(n)
            else:
                a[sum] = [n]

        sum = 0
        for n in range(len(nums)):
            sum += nums[n]
            es = a.get(sum-k)
            if es:
                for e in es:
                    if e < n:
                        ans += 1
            
        return ans
                
        
