# 문제 설명 : 각 cell에 명시된 화살표에 따라 (0,0) -> (M-1,N-1) 로 가야함. cost 1를 들여 화살표를 바꿀 수 있음.
# 최소 cost를 구하라.

# 나가거나 이미 방문한 곳을 돌아오려할때 signal를 바꿔보기? ㄴㄴ안됨.

# visited + 바꾸는 모든 경우를 bfs로 탐색? 추후에 재 방문했을때는 cost를 min하면?

# REMIND: 모든 경로를 저장해나아감. cost 가 적은 경우부터 priority queue? + visited.
# 한번 도달하면 바로 리턴

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        index_to_diff={1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}
        M, N = len(grid), len(grid[0])
        pq = [(0,0,0)] #(cost,x,y)
        visited = set() #(x,y)
        
        while pq:
            cost_, x_, y_ = heapq.heappop(pq)
            if (x_,y_) in visited: continue
            if x_ == M-1 and y_ == N-1: return cost_
            visited.add((x_,y_))
            for diff in [(0,1), (0,-1), (1,0), (-1,0)]:
                x, y = x_+diff[0], y_+diff[1]
                if 0<=x<M and 0<=y<N and (x,y) not in visited:
                    if diff != index_to_diff[grid[x_][y_]]: 
                        cost = cost_+1
                    else:
                        cost = cost_
                    heapq.heappush(pq,(cost,x,y))
        return 0