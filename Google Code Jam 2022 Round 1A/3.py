def solution():
    def solve():
        """
        lo[w][i][j] : i~j line에서의 weight w 의 min 값. 
        total[i][j] : i~j line에서의 모든 weight들의 합.
        dp[i][j] : i~j line을 진행할 수 있는 최소 횟수

        dp[i][j] = min(dp[i][k] + dp[k+1][j] for k in range(i, j)) - 2* total[i][j] 
        이 부분의 의미는
            - i~k 까지 진행 후, 모든 무게를 빼고, 다시 k+1~j를 진행한다. 
            - 이 부분에서 모든 무게를 뺴는것은 비효율적. 
            - (i~j line에서의 무게들의 최소값) 까지만 뺴면 그보다 더 무게를 뺼일은 절대 없다.
             => 이부분이 왜 항상 정답값, 최소임을 보장하는지는 모르겠다.
             
        """
        E, W = map(int, input().split())
        A = [[0 for _ in range(E)] for _ in range(W)]
        # minimum of weight w , case from e to k
        lo = [[[101 for _ in range(E)] for _ in range(E)] for _ in range(W)]

        for i in range(E):
            for w, a in enumerate(input().split()):
                A[w][i] = int(a)
        for w in range(W):
            for i in range(E):
                lo[w][i][i] = A[w][i]
                for j in range(i+1, E):
                    lo[w][i][j] = min(lo[w][i][j-1], A[w][j])
        # sum of minimum of all weights case from e to k
        total = [[0 for _ in range(E)] for _ in range(E)]
        for i in range(E):
            for j in range(E):
                s = 0
                for w in range(W):
                    s += lo[w][i][j]
                total[i][j] = s
        
        # dp
        dp = [[float('inf') for _ in range(E)] for _ in range(E)]
        for i in range(E): 
            dp[i][i] = 2*total[i][i]
        for l in range(1, E):
            for i in range(E):
                j = i+l
                if j < E:
                    dp[i][j] = min(list(dp[i][k] + dp[k+1][j] for k in range(i, j)) or [float('inf')]) - 2* total[i][j]
        return dp[0][E-1]


    for T in range(1,1+int(input())):
        ans = solve()
        print(f"Case #{T}: {ans}")

solution()
