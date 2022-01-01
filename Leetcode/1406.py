# 문제 해설: 돌을 1,2,3개중 가져가는데, 가져간 돌들의 values 가 최대가 되어야 한다. 
# 두 선수가 자기가 이길 수 있게 플레이했을때 이기게 되는 선수는?

# minmax
# Alice는 + 점수, Bob은 - 점수를 가진다고 가정하자.
# 합친 점수를 기록하여 0, 마이너스, 양수에 따라 이기는 사람이 정해짐. DP
# O(N) / O(N)

# REMIND : 겁나 어려웡... 하나의 점수로 합치기 위해 dp를 빼가면서 계산하는 방법이 핵심인듯.
# 두개가 나오면 애매함..

class Solution:
    def stoneGameIII(self, A: List[int]) -> str:
        N = len(A)
        dp = [0] * (N+1)
        for i in reversed(range(N)):
            dp[i] = max(sum(A[i:i+j+1])-dp[i+j+1] for j in (0,1,2) if i+j < N)
        return "Tie" if dp[0] == 0 else ("Alice" if dp[0] > 0 else "Bob")
            

    def stoneGameIII(self, A: List[int]) -> str:
        """
        답은 맞긴한데 시간 초과함.
        """
        N = len(A)
        
        @lru_cache(maxsize=None)
        def minmax(i: int, player: int) -> int:
            if i >= N:
                return 0
            if player == 0: #Alice
                return max(sum(A[i:i+x])+minmax(i+x, 1-player) for x in range(1, 4) if i+x <= N)
            else:
                return min(-sum(A[i:i+x])+minmax(i+x, 1-player) for x in range(1, 4) if i+x <= N)
        res = minmax(0, 0)
        return "Tie" if res == 0 else ("Alice" if res > 0 else "Bob")