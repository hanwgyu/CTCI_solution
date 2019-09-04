# Solution : 가장 긴 path를 찾아 중간 노드를 리턴.
# Time : O(N), Space : O(N)

from collections import defaultdict
from typing import Set

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(n : int, visited : Set[int]) -> List[int]:
            if n in visited:
                return []
            visited.add(n)
            p_1, p_2 = [], []
            for adj in graph[n]:
                p = dfs(adj, visited)
                if len(p) > len(p_1):
                    p_2 = p_1
                    p_1 = p
                elif len(p) > len(p_2):
                    p_2 = p
            h = len(p_1) + len(p_2) + 1
            if h > self.max_h:
                self.max_h = h
                self.max_p = p_1 + [n] + p_2[::-1]
            p_1.append(n)
            return p_1
   
        if not edges:
            return [0]
        self.max_h, self.max_p, graph = 0, None, defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        dfs(edges[0][0], set())
        return self.max_p[(self.max_h-1)//2 : self.max_h//2+1]
