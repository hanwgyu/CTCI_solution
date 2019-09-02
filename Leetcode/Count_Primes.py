# Solution : 에라토스테네스의 체.
# Time : O(NlogN), Space : O(N)

import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        nums = [True for _ in range(n)]
        nums[0], nums[1] = False, False
        for i in range(2, math.floor(math.sqrt(n))+1):
            if nums[i] == True:
                for j in range(i*2, n, i):
                    nums[j] = False
        return sum(nums)
            
