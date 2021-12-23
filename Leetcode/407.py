# 푸는 방법이 다르지만 결은 비슷하다. 높이가 낮은 노드부터 방문해서 가장 높은 노드는 나중에 방문해야 한다. 
# REMIND: 그냥 개어려움. 풀이봐도 이해안됨.

# 모든 블록을 방문해 위아래 양옆의 크기를 비교해 물의 양을 측정한다.
# 모든 노드를 다 바라보는건 비용이 크기 때문에, 모서리부터 시작해 heap을 사용해 가장 낮은 node부터 시작해 안쪽으로 체크해 나아간다.
# 높은 높이를 저장해나아감.

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        visited = defaultdict(bool)
        M, N = len(heightMap), len(heightMap[0])
        heap = []
        
        # Push all the block on the border into heap
        for i in range(M):
            for j in range(N):
                if i == 0 or j == 0 or i == M-1 or j == N-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[(i, j)] = True
                
        result = 0
        while heap:
            height, i, j = heapq.heappop(heap)    
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < M and 0 <= y < N and not visited[(x,y)]:
                    result += max(0, height-heightMap[x][y])
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))
                    visited[(x,y)] = True
        return result