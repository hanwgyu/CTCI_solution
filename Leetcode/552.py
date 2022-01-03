# DFS

#REMIND : dp 인데, 로직짜기가 되게 어렵다..

class Solution:
    def checkRecord(self, n: int) -> int:
        """
            DP
            
            1) A는 고려하지 않음.
            아래와 같은 문자로 끝나는 경우를 고려.
                       P (P+PL+PLL)
              P  ->   PL
             PL  ->  PLL
            PLL  -> PLLL  
            
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
            
            2) Absent 는 따로 계산
        """
        if n == 1: return 3
        dp = [1, 1, 2] # P로 끝나는 경우 (0, 1, 2 개)
        for i in range(3, n+1):
            dp.append((dp[i-1]+dp[i-2]+dp[i-3]) % 1000000007)
        
        # P로 끝나는 케이스들에 끝부분에 L를 더한다고 생각하면됨.
        res = (dp[n]+dp[n-1]+dp[n-2]) % 1000000007
        
        # A가 1개인 케이스 고려.
        # (0개 + A + n-1개), (1개 + A + n-2개), (2개 + A + n-3개), ... (n-1개 + A + 0개), ...케이스를 모두 더함.
        # i개 -> dp[i]+dp[i-1]+dp[i-2] = dp[i+1]
        for i in range(n):
            res += (dp[i+1]*dp[n-i]) % 1000000007
        return res % 1000000007
        
        
    
    def checkRecord_1(self, n: int) -> int:
        """
            DFS
        """
        @lru_cache(None)
        def dfs(i:int, cont_l: int, total_a:int) -> int:
            if total_a == 2 or cont_l == 3:
                return 0
            if i == n:
                return 1
            return (dfs(i+1, 0, total_a) + dfs(i+1, cont_l+1, total_a) + dfs(i+1, 0, total_a+1)) % 1000000007
        return dfs(0,0,0) % 1000000007