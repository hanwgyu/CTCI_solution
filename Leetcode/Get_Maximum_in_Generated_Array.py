# Time : O(N), Space: O(N)


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        a = [0, 1]
        for i in range(2, n + 1):
            a.append(a[i // 2] if i % 2 == 0 else a[i // 2] + a[i // 2 + 1])
        return max(a)
