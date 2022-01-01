# 왼쪽부터의 합을 새로 리스트로 만들고, 왼쪽부터 제거.

# REMIND: 진짜 어렵고 중요. 2 -> 3 번 해답으로 넘어가는 부분이 중요하다.

class Solution:
    def stoneGameVIII_3(self, A: List[int]) -> int:
        N = len(A)
        A = list(accumulate(A))
        ans = A[-1]
        for i in reversed(range(1, N-1)): # x > 1
            ans = max(ans, A[i]-ans)
            """
            원래는 2번과 같이 아래와 같이 계산된다.
            dp[i] = max(A[x]-dp[x] for x in range(i+1, N))
            =>
                dp[N-2] = max([A[N-1]])
                dp[N-3] = max([A[N-2]-dp[N-2], A[N-1]])
                dp[N-4] = max([A[N-3]-dp[N-3], A[N-2]-dp[N-2], A[N-1]])
                
            근데 보면 겹치기 때문에, 반복해서 연산해줄 필요가 없다.
                ans = max(A[N-1])
                ans = max(ans, A[N-2]-ans)
            """
        return ans
    
    def stoneGameVIII_2(self, A: List[int]) -> int:
        N = len(A)
        A = list(accumulate(A))
        dp = [0] * N
        dp[N-2] = A[N-1]
        for i in reversed(range(1, N-1)):
            dp[i] = max(A[x]-dp[x] for x in range(i+1, N))
            print(dp[i])
        return dp[0]
            
            
    def stoneGameVIII_1(self, A: List[int]) -> int:
        N = len(A)
        A = list(accumulate(A))
        
        @lru_cache(maxsize=None)
        def minmax(i: int) -> int:
            if i >= N-1:
                return 0
            res = max(B[x]-minmax(x) for x in range(i+1, N))
            return res
        return minmax(0)
