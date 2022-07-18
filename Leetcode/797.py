class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        acyclic이니 DFS로 돌면서 그냥 리턴. 
        """
        def dfs(src, dst) -> List[List[int]]:
            if src == dst:
                return [[src]]
            res = []
            for j in graph[src]:
                l = dfs(j, dst)
                for a in l:
                    res.append([src]+a)
            return res
        return dfs(0, len(graph)-1)
