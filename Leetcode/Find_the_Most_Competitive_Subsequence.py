# Solution : 남아있는 갯수와 스택 사이즈를 고려해 최대한 작은 값을 스택 앞쪽에 저장.
# Time : O(N), Space: O(k)


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        s = []
        for i, n in enumerate(nums):
            while s and s[-1] > n and len(nums) - i > k - len(s):
                s.pop()
            if len(s) < k:
                s.append(n)
        return s
