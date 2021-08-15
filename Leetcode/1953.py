# Time : O(N), Space: O(1)

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        s, m = sum(milestones), max(milestones)
        return s if s - m + 1 >= m else 2 * (s-m) + 1
