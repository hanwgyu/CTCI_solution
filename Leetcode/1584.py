class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Prim's algorithm
        구름을 퍼트리듯이, 임의의 노드에서 시작해 노드들과 연결된 vertex들 중 가장 짧은 것을 추가한다. 
        한 노드를 두번 방문은 하지 않기 때문에 사이클이 생기지 않는다.
        heap 사용.
        
        O((E+V)logV) / O(E)
        """
        def distance(point1: List[int], point2: List[int]) -> int:
            return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])
            
        visited = set()
        N = len(points)
        h = [(0, 0)] # heap, start from node 0. (dist, node)
        
        ans = 0
        while len(visited) != N:
            dis, i = heapq.heappop(h)
            if i in visited:
                continue
            ans += dis
            visited.add(i)
            # append edges
            for k in range(N):
                if k not in visited:
                    heapq.heappush(h, (distance(points[i], points[k]), (k)))
        return ans
    
    def minCostConnectPoints_1(self, points: List[List[int]]) -> int:
        """
        Kruskal's algorithm
        짧은 순서대로 edge를 찾고, cycle을 만들지 않으면 추가한다. 
        
        Union-Find를 사용해 cycle이 생기는지를 판단한다.
        
        O(N^2logN) / O(N^2)
        """
        N = len(points)
        d = defaultdict(int)
        h = [0 for _ in range(N)]
        for i in range(N):
            d[i] = i
             
        def union(i1: int, i2: int):
            g1, g2 = find(i1), find(i2)
            if g1 != g2:
                # union-by-rank 
                if h[g1] > h[g2]:
                    d[g2] = g1
                elif h[g1] == h[g2]:
                    d[g2] = g1
                    h[g1] += 1
                else:
                    d[g1] = g2
        
        def find(i: int) -> int:
            if d[i] == i:
                return i
            g = find(d[i])
            # path-compression
            d[i] = g
            return g
             
        edges = [(abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]), (i,j)) for i in range(N) for j in range(i+1, N)]
        edges.sort()
        
        ans = 0
        for cost, (i,j) in edges:
            if find(i) == find(j):
                continue
            union(i,j)
            ans += cost
        return ans
        