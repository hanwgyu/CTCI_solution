# Brute-force. O(N^2), O(1)

# Solution : Even sum과 odd sum들을 저장해놓고, index를 기준으로 뒷부분은 odd sum과 even sum을 뒤집어서 더해줌.
# Time : O(N), Space : O(N)


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_sums, odd_sums = [0], [0]
        even_sum, odd_sum = 0, 0
        ans = 0
        for i, n in enumerate(nums):
            if i % 2 == 0:
                even_sum += n
                even_sums.append(even_sum)
            else:
                odd_sum += n
                odd_sums.append(odd_sum)
        for i in range(len(nums)):
            even = even_sums[(i + 1) // 2] + (odd_sum - odd_sums[(i + 1) // 2])
            odd = odd_sums[i // 2] + (even_sum - even_sums[(i + 2) // 2])
            if even == odd:
                ans += 1
        return ans
