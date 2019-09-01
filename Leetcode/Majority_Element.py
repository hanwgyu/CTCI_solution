# Solution 1 : Hash. 
# Time : O(N), Space : O(N)

# Solution 2 : Sorting. 
# Time O(NlogN), Space : O(N)

# Solution 3 : Bit Manipulation. 과반수 이상인 원소가 존재하므로, 과반수 이상으로 카운트 된 bit만 모으면 해당 원소를 표현가능.
# Time : O(N), Space : O(1)

# Solution 4 : Boyd-Moore voting algorithm. 값이 다른 두 원소를 지워가다보면, 과반수 이상인 원소가 남게됨.
# Time : O(N), Space : O(1)

from collections import defaultdict

class Solution:
    def majorityElement_4(self, nums: List[int]) -> int:
        ans, cnt = 0, 0
        for num in nums:
            if cnt == 0:
                ans = num
            cnt = cnt + 1 if ans == num else cnt - 1
        return ans
    
    def majorityElement_3(self, nums: List[int]) -> int:
        # 32bit integer
        bits = [0 for _ in range(32)]
        for num in nums:
            for i in range(32):
                bits[i] += (num >> i) & 1     
        ans = 0
        for i, bit in enumerate(bits):
            if bit >= (len(nums)+1)//2:
                ans += 1 << i
                if i == 31:
                    ans = ~(ans ^ 0xFFFFFFFF)
        return ans
    
    
    def majorityElement_2(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
    
    
    def majorityElement_1(self, nums: List[int]) -> int:
        d, ret = defaultdict(lambda: 0), 0
        for num in nums:
            d[num] += 1
            if d[num] >= (len(nums)+1)//2:
                ret = num
                break
        return ret
