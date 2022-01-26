# 문제 설명 : 비어있는 공간에 건물을 짓는데, 다른 건물들과의 거리합이 최소인 곳!

# REMIND : 기본 문제 (bfs+visited)도 어렵고, 거기서 머리를 잘써서 케이스를 줄이는것도 너무 어렵다.

class Solution:    
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
            시작 좌표를 빌딩이 있는 곳에서 시작해서, 각 좌표에 방문 횟수를 기록함.
            방문횟수가 현재까지 빌딩 시작 횟수와 같지 않으면 방문못한 좌표이므로 아예 제거해버린다.
            이게 더 빠르게 많은 케이스를 빼버릴 수 있음.
        """
        M, N = len(grid), len(grid[0])
        B = sum(1 for i in range(M) for j in range(N) if grid[i][j] == 1)
        
        total_visited = defaultdict(int) # (i,j)에 방문한 횟수 기록
        distance = defaultdict(int) # (i,j)까지의 distance 합을 기록
        self.b = 0
        
        def bfs(si: int, sj: int) -> int:
            q, res, visit = deque([(si,sj,0)]), 0, set([(si,sj)])
            while q:
                i, j, l = q.popleft()
                for diff in [(0,-1), (0,1), (-1,0), (1,0)]:
                    i_,j_ = i+diff[0],j+diff[1]
                    if 0<=i_<M and 0<=j_<N and (i_,j_) not in visit and total_visited[(i_,j_)] == self.b:
                        visit.add((i_,j_))
                        if grid[i_][j_] == 0:
                            distance[(i_,j_)] += l+1
                            total_visited[(i_,j_)] += 1
                            q.append((i_,j_,l+1))
            self.b+=1

        #REMIND : min내에 값이 empty array일경우 뒤의 원소로 계산하게됨.
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    bfs(i, j)
        return min(list(distance[(i, j)] for i in range(M) for j in range(N) if total_visited[(i,j)] == B) or [-1])
        
        
    
    
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
            일단 모든 좌표에서 비교해야함.
            bfs+visited로 돌면서 최소 거리의 합을 구함.
            
            + 시간을 더 줄이기위해서
            빌딩을 모두 방문하지 못한 좌표는 아예 방문하지 않게 뺴버린다.그와 연결된 좌표들도 어짜피 이미 방문 못했어서. 상관없다.
            이래도 여전히 시간이 오래걸린다.
        """
        M, N = len(grid), len(grid[0])
        B = sum(1 for i in range(M) for j in range(N) if grid[i][j] == 1)
        impossible = set()

        def bfs(si: int, sj: int) -> int:
            n, q, res, visit = 0, deque([(si,sj,0)]), 0, set([(si,sj)])
            while q and n != B:
                i, j, l = q.popleft()
                if grid[i][j] == 1:
                    n, res = n+1, res+l
                if grid[i][j] != 0:
                    continue
                for diff in [(0,-1), (0,1), (-1,0), (1,0)]:
                    i_,j_ = i+diff[0],j+diff[1]
                    if 0<=i_<M and 0<=j_<N and (i_,j_) not in visit and (i_,j_) not in impossible:
                        q.append((i_,j_,l+1))
                        visit.add((i_,j_))
            if n != B:
                impossible.add((si,sj))
            return res if n == B else float('inf')

        #REMIND : min내에 값이 empty array일경우 뒤의 원소로 계산하게됨.
        ans = min(list(bfs(i, j) for i in range(M) for j in range(N) if grid[i][j] == 0) or [float('inf')])
        return ans if ans != float('inf') else -1