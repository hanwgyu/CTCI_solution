class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        M, N = len(rowSum), len(colSum)
        ans = [[0 for _ in range(N)] for _ in range(M)]
        for j in range(N):
            for i in range(M):
                ans[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= ans[i][j]
                colSum[j] -= ans[i][j]
        return ans
