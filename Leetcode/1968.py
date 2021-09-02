# 모든 조합에 대해 체크
# Time : O(N!*N) , Space: O(1)

# 고민 2 : 양옆의 값이 가운데 값보다 모두 작거나 크면 average를 절대 만족하지 못한다.
# Time : O(NlogN), Space: O(1)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        i, j = 0, len(nums) - 1
        while i <= j:
            l, r = nums[i], nums[j]
            if i != j:
                ans.append(l)
            ans.append(r)
            i, j = i+1, j-1
        return ans

    def rearrangeArray_1(self, nums: List[int]) -> List[int]:
        def check(nums: List[int]) -> bool:
            return all((nums[i-1] + nums[i+1] != 2 * nums[i]) for i in range(1, len(nums)-1))

        for l in itertools.permutations(nums):
            if check(l):
[?12;4$y                return l
        return None

