# * 를 관리하는 부분이 어려움. 문자 갯수가 몇개인지 모르니.
# dfs로 매칭되는 모든 패턴을 체크

# REMIND : 간단하나 중요한 기본 dfs 문제.
# O(MN) / O(MN)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        DP로 푸는게 훨씬 쉽긴하다.
        """
        dp = defaultdict(bool)
        M, N = len(s), len(p)
        dp[(0,0)] = True
        # 예외 처리
        for j in range(1, N+1):
            if p[j-1] != '*':
                break
            dp[(0, j)] = True
        
        for j, n in enumerate(p, start=1):
            for i, m in enumerate(s, start=1):
                if n == '*':
                    dp[(i,j)] = dp[(i-1, j-1)] or dp[(i-1,j)] or dp[(i,j-1)]
                elif n in ('?', m):
                    dp[(i,j)] = dp[(i-1, j-1)]
        return dp[(M, N)]
        
         

            
    
    def isMatch1(self, s: str, p: str) -> bool:
        M, N = len(s), len(p)
        @lru_cache(None)
        def dfs(i: int, j: int) -> bool:
            if i >= M or j >= N:
                if i >= M and j >= N:
                    return True
                # 이부분에 대한 예외처리가 중요하다. 마지막 부분에 *가 오는 경우.
                if i >= M and p[j] == '*':
                    return dfs(i, j+1)
                return False
            m, n = s[i], p[j]
            if n == '*':
                return any([dfs(i, j+1), dfs(i+1, j), dfs(i+1, j+1)])
            elif n == '?':
                return dfs(i+1, j+1)
            else:
                return dfs(i+1, j+1) if m == n else False 
        return dfs(0, 0)