# Time : O(N), Space : O(1)

from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d = defaultdict(int)
        A, B = 0, 0
        for i in range(len(guess)):
            m, n = secret[i], guess[i]
            if m == n:
                A += 1
            else:
                d[m] += 1
                d[n] -= 1
                if d[m] <= 0:
                    B += 1
                if d[n] >= 0:
                    B += 1
        return "{}A{}B".format(A, B)
