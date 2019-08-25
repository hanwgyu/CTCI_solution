# Solution1 : 값을 표시하는 Vertex to Vertex list를 만들고, 모든 노드에서 모든 노드까지 경로값을 업데이트. 중간 노드에 대해 iteration. Floyd-Warshall과 동일한 방식.
# hash의 hash를 사용하여 경로값을 표시.
# Time : O(V^3), Space : O(V^2)

from collections import defaultdict

class Solution:



    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        vals = defaultdict(lambda: defaultdict(lambda: -1.0))
        inputs = defaultdict()
        for i in range(len(equations)):
            src, dst, val = equations[i][0], equations[i][1], values[i]
            vals[src][dst] = val
            vals[dst][src] = 1.0 / val
            inputs[src] = True
            inputs[dst] = True
        
        for src in inputs.keys():
            for dst in inputs.keys():
                if src == dst:
                    vals[src][dst] = 1.0
                    continue
                elif src in vals and dst in vals[src]:
                    continue
                for mid in inputs.keys():
                    if src in vals and mid in vals[src] and mid in vals and dst in vals[mid]:
                        res = vals[src][mid] * vals[mid][dst]
                        vals[src][dst] = res
                        break
                        
        return [vals[query[0]][query[1]] for query in queries]
                        
        
