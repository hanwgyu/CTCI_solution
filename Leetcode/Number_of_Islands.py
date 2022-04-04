from collections import defaultdict

class Solution:
    def numIslands(self, A: List[List[str]]) -> int:
        """
        BFS
        모든 원소가 1이여도, bfs로 진행시 대각선에 해당하는 만큼만 한번에 저장하게 되어 공간을 엄청 줄일 수 있다!!!!!
        
        O(MN) / O(min(M,N))
        """
        q = deque()
        ans = 0
        M, N = len(A), len(A[0])
        for j in range(N):
            for i in range(M):
                if A[i][j] != "0":
                    ans += 1
                    A[i][j] = "0"
                    q.append((i,j))
                while q:
                    it, jt = q.popleft()
                    for diff in [(0,-1), (0,1), (-1,0), (1,0)]:
                        i_, j_ = it+diff[0], jt+diff[1]
                        if 0<=i_<M and 0<=j_<N and A[i_][j_] != "0":
                            A[i_][j_] = "0"
                            q.append((i_,j_))
        return ans
    
    def numIslands(self, A: List[List[str]]) -> int:
        """
        DFS
        
        O(MN) / O(MN)
        """
        def dfs(i: int, j: int) -> int:
            if A[i][j] == "0":
                return 0
            A[i][j] = "0"
            for diff in [(-1,0), (1,0), (0,-1), (0,1)]:
                i_, j_ = i+diff[0], j+diff[1]
                if 0 <= i_ < len(A) and 0 <= j_ < len(A[0]):
                    dfs(i_, j_)
            return 1
        ans = 0
        M, N = len(A), len(A[0])
        for j in range(N):
            for i in range(M):
                ans += dfs(i, j)
        return ans
