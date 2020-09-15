# Solution
# Time : O(1), Space: O(1)

from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_sec = -1
        ret = ""
        for a, b, c, d in permutations(A):
            if a * 10 + b < 24 and c * 10 + d < 60:
                sec = a * 10 * 60 + b * 60 + c * 10 + d
                if max_sec < sec:
                    max_sec = sec
                    ret = "{}{}:{}{}".format(a, b, c, d)
        return ret
