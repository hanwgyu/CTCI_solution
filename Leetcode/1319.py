class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        Group으로 연결후 (총 group의 갯수 - 1)
        """
        if len(connections) < n-1:
            return -1
        visited = set()
        adj_list = defaultdict(list)
        for i, j in connections:
            adj_list[i].append(j)
            adj_list[j].append(i)
        
        def visit(node):
            if node in visited:
                return
            visited.add(node)
            for j in adj_list[node]:
                visit(j)
        
        ans = 0
        for i in range(n):
            if i not in visited:
                ans += 1
                visit(i)
        return ans-1
                