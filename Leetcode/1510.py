# 문제 설명 : 제곱 갯수만큼 움직이고, 마지막에 움직이지 못하면 지게됨.

# 1씩이라도 움직일 수 있음.
# REMIND: 결과는 마지막에 나온다.

import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(maxsize=None)
        def minmax(i: int, player: int) -> bool:
            """
                i: 시작 index
                player: (0: Alice, 1: Bob)
                
                return True if player can win
            """
            if i == n:
                return False
            m = int(math.sqrt(n-i))
            if m*m == n:
                return True
            return not all(minmax(i+x*x, 1-player) for x in reversed(range(1,m+1)))
        return minmax(0, 0)