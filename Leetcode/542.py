class Solution:
    def updateMatrix(self, A: List[List[int]]) -> List[List[int]]:
        """
        BFS의 정석 문제.
        
        모든 0들을 Queue에 넣어놓고 시작한다. 방문한 노드는 다시 방문하지 않는다.

        O(MN) / O(MN)
        """
        M, N = len(A), len(A[0])
        q, visited = deque(), set()
        for i in range(M):
            for j in range(N):
                if A[i][j] == 0:
                    q.append((i,j,0))
                    visited.add((i,j))
        while q:
            i, j, d = q.popleft()
            A[i][j] = d
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                pi, pj = i+di, j+dj
                if 0 <= pi < M and 0<= pj < N and (pi, pj) not in visited:
                    q.append((pi,pj,d+1))
                    visited.add((pi,pj))
        return A
    
    def updateMatrix(self, A: List[List[int]]) -> List[List[int]]:
        """
        DP.
        
        왼쪽 위에서 시작하는 것과 오른쪽 아래에서 시작하는것을 두번하면, 모든 네 방향에서의 min값을 구할 수 있다.
      
        inplace로 해서 space를 줄임.

        O(MN) / O(1)
        """
        M, N = len(A), len(A[0])
        for i in range(M):
            for j in range(N):
                if A[i][j] == 1:
                    A[i][j] = float('inf')
        for i in range(M):
            for j in range(N):
                if A[i][j] > 0:
                    top = A[i-1][j]+1 if i > 0 else float('inf')
                    left = A[i][j-1]+1 if j > 0 else float('inf')
                    A[i][j] = min(A[i][j], top, left)
    
        for i in reversed(range(M)):
            for j in reversed(range(N)):
                if A[i][j] > 0:
                    down = A[i+1][j]+1 if i+1 < M else float('inf')
                    right = A[i][j+1]+1 if j+1 < N else float('inf')
                    A[i][j] = min(A[i][j], down, right)
        return A
