# frequency가 겹친 문자들을 최소한 줄여서 겹치지 않는 곳에 넣음.
# Time : O(N), Space : O(1)

from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        cnts = Counter(s)
        freqs = set()
        ans = 0
        for freq in cnts.values():
            while freq > 0 and freq in freqs:
                freq, ans = freq - 1, ans + 1
            freqs.add(freq)
        return ans
