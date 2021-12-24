# 모든 방향으로 + visited
# bfs로 이동하면 step이 작은 순서대로 이동해서 제대로 나오게됨. (이 로직을 이해하는게 제일 중요하다. )
# REMIND: 어려움. 이 패턴에 익숙해져야함.

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dq = deque([(0,0,0,0)]) # (x,y,r,step)
        visited = set([(0,0,0)]) # (x,y,r) 
        M, N = len(grid), len(grid[0])
        if M == 1 and N == 1:
            if grid[0][0] == 1 and k == 0:
                return -1
            return 0
        while dq:
            x_,y_,r_,step_ = dq.popleft()
            for diff in [(-1,0), (1,0), (0,-1), (0,1)]:
                x,y,r,step = x_,y_,r_,step_ 
                x, y, step = x+diff[0], y+diff[1], step+1
                if x < 0 or x >= M or y < 0 or y >= N:
                    continue
                if grid[x][y] == 1:
                    r += 1
                if  r > k or (x,y,r) in visited:
                    continue
                if x == M-1 and y == N-1:
                    return step
                visited.add((x,y,r))
                dq.append((x,y,r,step))
        return -1