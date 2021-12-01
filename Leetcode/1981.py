# 고민 1: 모든 경우의 수 계산?
# Time : O(M*N^M), Space : O(1)
# Time limit exceeded

# 고민 2: set으로 합을 저장해 계산량을 줄임

class Solution:
    def minimizeTheDifference(self, mat, target):
        nums = {0}
        for row in mat:
            nums = {x + i for x in row for i in nums}

        return min(abs(target - x) for x in nums)

    def minimizeTheDifference_1(self, mat: List[List[int]], target: int) -> int:
        M, N = len(mat), len(mat[0])
        ans = float('inf')
        for l in product(range(N), repeat=M):
            ans = min(ans, abs(sum(mat[i][j] for i, j in enumerate(l)) - target))
        return ans
