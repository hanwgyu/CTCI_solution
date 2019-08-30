# Time : O(N), Space : O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0 for _ in range(32)]
        for num in nums:
            for i in range(32):
                bits[i] += (num >> i) & 1
        ans = 0
        for i, bit in enumerate(bits):
            if bit % 3 == 1:
                ans = ans | 1 << i
                if i == 31:
                    ans = ~(ans ^ 0xFFFFFFFF)        
        return ans
    
