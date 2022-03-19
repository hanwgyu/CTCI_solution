# Solution 1 : Hash.
# Time : O(N), Space : O(N)

# Solution 2 : Sorting.
# Time O(NlogN), Space : O(N)

from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        절반보다 많다면 값이 다르면 count를 뺴주는 식으로 O(1)으로 구해낼 수 있다. 

        O(N) / O(1)
        """
        ans, cnt = None, 0
        for n in nums:
            if cnt == 0:
                ans = n
            cnt = cnt+1 if ans == n else cnt-1
        return ans

    def majorityElement_3(self, nums: List[int]) -> int:
        """
        Bit Manipulation.
        32 비트를 쪼개서 count 갯수를 저장.
        특정 원소가 과반수 초과이므로, count가 과반수 초과인 것만 골라내면 됨.
        다른 원소들이 아무리 합쳐져도 과반수 이하여서 문제 없다.

        O(N) / O(1)
        """
        # 32bit integer
        bits = [0 for _ in range(32)]
        for num in nums:
            for i in range(32):
                bits[i] += (num >> i) & 1
        ans = 0
        for i, bit in enumerate(bits):
            if bit >= (len(nums) + 1) // 2:
                ans += 1 << i
                if i == 31:
                    ans = ~(ans ^ 0xFFFFFFFF)
        return ans

    def majorityElement_2(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

    def majorityElement_1(self, nums: List[int]) -> int:
        d, ret = defaultdict(lambda: 0), 0
        for num in nums:
            d[num] += 1
            if d[num] >= (len(nums) + 1) // 2:
                ret = num
                break
        return ret
