# Solution 0 : Heuristics. 특정 index의 양옆의 index를 저장하는 list를 둠. 특정 원소 pop되면 해당 list를 수정. Time : O(N!), Space : O(N)

# Solution 1 : 아무것도 없는 상황에서 풍선을 추가해나아감. Recursive.
# Function 'maxCoinsRange(l, r)' : index l+1~r-1까지의 ballon을 추가해나아가는 최대 coin을 리턴.
# Time : O(?), Space : O(N^2) (Worst Case에서 Recursive하게 N, N-1,.... 1의 메모리가 쌓임)
# Leet code Time Limit Exceeded.

# Solution 2 : Solution 1 + DP.
# Time : O(N^3), Space : O(N^2)


class Solution:
    def maxCoins_2(self, nums: List[int]) -> int:
        def maxCoinsRange(l: int, r: int) -> int:
            if l + 1 == r:
                return 0
            if (l, r) in d:
                return d[(l, r)]
            res = max(
                nums[l] * nums[r] * nums[i]
                + maxCoinsRange(l, i)
                + maxCoinsRange(i, r)
                for i in range(l + 1, r)
            )
            d[(l, r)] = res
            return res

        d = {}
        nums.append(1)
        nums.insert(0, 1)
        return maxCoinsRange(0, len(nums) - 1)

    def maxCoins_1(self, nums: List[int]) -> int:
        def maxCoinsRange(l: int, r: int) -> int:
            if l + 1 == r:
                return 0
            return max(
                nums[l] * nums[r] * nums[i]
                + maxCoinsRange(l, i)
                + maxCoinsRange(i, r)
                for i in range(l + 1, r)
            )

        nums.append(1)
        nums.insert(0, 1)
        return maxCoinsRange(0, len(nums) - 1)
