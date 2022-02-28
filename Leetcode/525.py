class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Prefix Sum.
        1과 0의 갯수 차이의 존재 여부를 저장해나아감.
        O(N) / O(N)
        """
        ans, diff = 0, 0
        d = defaultdict(int) #key: 1,0갯수 차이, value: index의 최솟값
        d[0] = -1
        for i, n in enumerate(nums):
            diff = diff+1 if n == 1 else diff-1
            if diff not in d:
                d[diff] = i
            if diff in d:
                ans = max(ans, i-d[diff])
        return ans