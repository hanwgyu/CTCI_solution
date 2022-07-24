class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        개 신기함.
        visited[node] 에 모든 경로에 대한 visited 리스트를 bit 형태로 저장.
        그리고서 모든 케이스를 BFS로 돌면서, 처음 모든 노드를 방문할때 리턴.
        """
        visited = defaultdict(lambda: set())
        q = []
        N = len(graph)
        for i in range(N):
            visited[i].add(1<<i)
            q.append([i, 1<<i])
        res = 0
        while q:
            res += 1
            new_q = []
            for i, val in q:
                for j in graph[i]:
                    next_val = (1<<j) | val
                    if next_val not in visited[j]:
                        if next_val+1 == 1<<N:
                            return res
                        visited[j].add(next_val)
                        new_q.append([j, next_val])
            q = new_q
        return 0
