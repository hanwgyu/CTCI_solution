class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        """
        DP + sort
        """
        rides.sort(key=lambda e: (e[1],e[0],e[2]))
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            for s, t in d[i]:
                dp[i] = max(dp[i], dp[s]+t)
            dp[i] = max(dp[i], dp[i-1])
        return dp[-1]    
    
    def maxTaxiEarnings1(self, n: int, rides: List[List[int]]) -> int:
        """
        DP 
        - end 위치에 cost를 max로 저장. end까지 실행했을때 최대cost.
        - start가 실행되기 전에 이전 end까지 모두 실행해야함.
          - end 가 커지는 순서대로 sorting해 실행
        """
        d = defaultdict(list)
        for s, e, t in rides:
            d[e].append([s, e-s+t])
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            for s, t in d[i]:
                dp[i] = max(dp[i], dp[s]+t)
            dp[i] = max(dp[i], dp[i-1])
        return dp[-1]
