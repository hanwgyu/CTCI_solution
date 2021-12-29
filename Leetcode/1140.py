# alice 가 가지게되는 최대의 돌 갯수를 리턴.
# 내 현상황에서 모든 케이스를 고려해 계산
# Remind: lru_cache

class Solution:
    def stoneGameII(self, A: List[int]) -> int:
        @lru_cache(maxsize=None)
        def minmax(i: int, m: int, player: int) -> int:
            """
                player : (0: Alice, 1: Bob)
            """
            N = len(A)
            if i >= N:
                return 0
            if player == 0:
                return max(sum(A[i:i+x])+minmax(i+x, max(m,x), 1-player) for x in range(1, 2*m+1) if i+x <= N)
            else:
                return min(minmax(i+x, max(m,x), 1-player) for x in range(1, 2*m+1) if i+x <= N)

        return minmax(0, 1, 0)