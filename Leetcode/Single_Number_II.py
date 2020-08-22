# Solution 1: Bit manipulation
# Time : O(N), Space : O(1)

# Solution 2: 1을 반복 추가했을때, (ans, seen) : (0,0) -> (1,1) -> (1,0) -> (0,1) ->  (0,0)
# Time : O(N), Space : O(1)

# Solution 3: 1을 반복 추가했을때, (1mod3, 2mod3) : (0,0) -> (1,0) -> (0,1) -> (0,0)
# Time : O(N), Space : O(1)


class Solution:
    def singleNumber_3(self, nums: List[int]) -> int:
        one_mod3, two_mod3 = 0, 0
        for num in nums:
            one_mod3 = (one_mod3 ^ num) & ~two_mod3
            two_mod3 = (two_mod3 ^ num) & ~one_mod3
        return one_mod3

    def singleNumber_2(self, nums: List[int]) -> int:
        seen, ans = set(), 0
        for num in nums:
            if num not in seen:
                seen.add(num)
                ans ^= num
            else:
                seen.remove(num)
        return ans

    def singleNumber_1(self, nums: List[int]) -> int:
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
