# 0->1로 최대 한번 바꿔서 만들 수 있는 '1'로 구성된 섬의 최대 크기

# T1) 섬의 크기를 구할 수 있는 법? 
# 방문한 노드 저장, dfs

# T2) 변경할 0의 위치를 구할 수 있는 방법?
# 모든 경우에 대해 T1을 트라이
# Union-find

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        모든 경우를 다 계산.
        섬의 index를 두고, grid의 값을 index로 바꾸면서 진행. (횟수를 크게 줄일 수 있음)
        """
        N = len(grid)
        
        def neighbors(x, y):
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x+i < N and 0 <= y+j < N:
                    yield x+i, y+j
                    
        def dfs(x, y, index) -> int:
            res = 0
            grid[x][y] = index
            for i, j in neighbors(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res+1
    
    
        # Find islands
        index = 2
        areas = {0:0} # index: area
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    areas[index] = dfs(x, y, index)
                    index += 1
        
        # Change 0 -> 1
        res = max(areas.values())
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    indexes = set(grid[i][j] for i, j in neighbors(x,y))
                    res = max(res, sum(areas[index] for index in indexes) + 1)
        return res  
                        
                
                