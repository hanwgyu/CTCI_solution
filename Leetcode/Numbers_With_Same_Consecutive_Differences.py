# Solution 1:
# Time : O(N), Space: O(N


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        ret = []

        def getDiffs(n: int, K: int) -> List[int]:
            diffs = []
            if K == 0:
                return [n]
            if n - K > -1:
                diffs.append(n - K)
            if n + K < 10:
                diffs.append(n + K)
            return diffs

        def dfs(cur_N: int, num: int, N: int, K: int):
            if cur_N == N:
                ret.append(num)
                return
            for diff in getDiffs(num % 10, K):
                dfs(cur_N + 1, 10 * num + diff, N, K)

        if N == 1:
            ret.append(0)
        for i in range(1, 10):
            dfs(1, i, N, K)
        return ret
