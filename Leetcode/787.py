class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        Bellman Ford.
        각 step에서 모든 edge를 iterate 하면서 값을 업데이트.
        주의) step마다 임시 값을 저장해놓고 한번에 업그레이드해야함.
        """
        adj_list = defaultdict(list)
        for i, j, cost in flights:
            adj_list[i].append((j, cost))
        
        costs = defaultdict(lambda : float('inf'))
        costs[src] = 0
        
        temp = copy.deepcopy(costs)
        for _ in range(K+1):
            for i, l in adj_list.items():
                for j, cost in l:
                    temp[j] = min(temp[j], costs[i]+cost)
            costs = copy.deepcopy(temp)
        return costs[dst] if costs[dst] != float('inf') else -1
        
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
      """
      BFS.
      cost가 작은 위치를 저장. dst 가장 먼저 방문하면 바로 리턴.
      """
        path = defaultdict(list)
        visited = {}
        for s, d, c in flights:
            path[s].append((d,c))
        
        heap = [(0, src, K+1)]
        while heap:
            cost, s, k = heapq.heappop(heap)
            if s == dst:
                return cost
            if k > 0 and (s not in visited or visited[s] < k):
                visited[s] = k 
                for d, c in path[s]:
                    heapq.heappush(heap, (cost+c, d, k-1))
        return -1
        
    
    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        dfs
        """
        path = defaultdict(list)
        for s, d, c in flights:
            path[s].append((d,c))
        
        def dfs(src, dst, c, K, visited) -> int:
            if src == dst:
                return c
            if src in visited or K < 0:
                return float('inf')
            visited.add(src)
            ans = min(list(dfs(d, dst, c+cost, K-1, visited) for d, cost in path[src]) or [float('inf')])
            visited.remove(src)
            return ans
        ans = dfs(src, dst, 0, K, set())
        return -1 if ans == float('inf') else ans 
