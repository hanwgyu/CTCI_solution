# 문제 해설 : 오른쪽 아래로 움직이면서 체력이 깎이고 회복되는데, 초창기 최소 체력을 구하라

# 걍 DP. 거꾸로 오면서 필요한 최소 체력을 dp로 업데이트해감.
# 거꾸로 온다는걸 인지하는게 중요함. 근데 어렵지 않다.

# O(MN) / O(MN)
# O(MN) / O(M) 으로 줄일 수 있다.

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M, N = len(dungeon), len(dungeon[0])
        res = float('inf')
        dp = [[float('inf') for _ in range(N+1)] for _ in range(M+1)]
        dp[M][N-1] = 1
        for j in reversed(range(N)):
            for i in reversed(range(M)):
                dp[i][j] = max(1, min(dp[i][j+1], dp[i+1][j])-dungeon[i][j])
        return dp[0][0]