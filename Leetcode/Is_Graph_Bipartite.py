# Solution 2 : 입력 'graph'를 iteration돌면서, src와 dsts들을 항상 다른 group으로 추가함.
# 1)dst의 group을 정하기 위해, iteration돌면서 src나 dsts중 특정 그룹에 포함된 노드가 있는지 파악.
# 2)없으면 issue_group하여 새롭게 그룹을 배정. 추후에 상황에 따라 defaultGroup으로 변경.
# iteration도는 와중에 src와 dst가 같은 그룹에 속하면 return False.
# Time : O(|V| + |E|), Space : O(|V|)

from collections import defaultdict


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node: int) -> bool:
            for i in graph[node]:
                if i in color:
                    if color[i] == color[node]:
                        return False
                else:
                    color[i] = 1 - color[node]
                    if not dfs(i):
                        return False
            return True

        color = dict()
        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                if not dfs(node):
                    return False
        return True

    def isBipartite_2(self, graph: List[List[int]]) -> bool:
        def changeGroup(from_g: int, to_g: int):
            for v, g in v_to_g.items():
                if g == from_g:
                    v_to_g[v] = to_g

        def getPairGroup(g: int) -> int:
            if g % 2 == 0:
                return g + 1
            else:
                return g - 1

        # Default Group : (0, 1), extra group : (2, 3), (4, 5), ...
        v_to_g = defaultdict(int)
        issue_g = 0
        for src, dsts in enumerate(graph):
            dst_g = -1
            if src in v_to_g:
                dst_g = getPairGroup(v_to_g[src])
            else:
                for dst in dsts:
                    if dst in v_to_g:
                        dst_g = v_to_g[dst]
                        break
                if dst_g == -1:
                    dst_g = issue_g
                    issue_g += 2
                v_to_g[src] = getPairGroup(dst_g)

            for dst in dsts:
                if dst in v_to_g:
                    if getPairGroup(dst_g) == v_to_g[dst]:
                        return False
                    elif v_to_g[dst] != dst_g:
                        changeGroup(v_to_g[dst], dst_g)
                    continue
                v_to_g[dst] = dst_g
        return True
