# 고민 1 : 그래프와 동일. src -> dst로 가는 경로의 값들을 곱함.
# 어떻게 경로를 찾을지가 고민.
# 먼저 모두 dfs로 iteration돌면서 값 넣기. 값이 있으면 pass
# sorting없는 일종의 다익스트라. 방문하지 않은 노드를 방문.

# 고민 2: 깔끔하게 정리. + floyd-warshall 적용
# ref : https://leetcode.com/problems/evaluate-division/discuss/88175/9-lines-%22Floydu2013Warshall%22-in-Python

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(defaultdict(lambda: -1.0))
        for (src, dst), val in zip(equations, values):
            d[src][src] = quot[dst][dst] = 1.0
            d[src][dst] = val
            d[dst][src] = 1 / val
        for k, i, j in itertools.permutations(quot, 3):
            d[i][j] = d[i][k] * d[k][j]
        return [d[src][dst] for src, dst in queries]


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(list) #
        v = defaultdict(lambda : -1) # key : (src, dst)
        for i, (src, dst) in enumerate(equations):
            d[src].append(dst)
            d[dst].append(src)
            v[(src,dst)] = values[i]
            v[(dst,src)] = 1.0/values[i]
            v[(src,src)] = 1.0
            v[(dst,dst)] = 1.0

        def dfs(src, dst, value, start=False):
            if not start and v[(src,dst)] != -1.0:
                return
            v[(src,dst)] = value
            for new_dst in d[dst]:
                new_value = value * v[(dst, new_dst)]
                dfs(src, new_dst, new_value)

        for src, dsts in d.items():
            for dst in dsts:
                dfs(src, dst, v[(src,dst)], True)

        return [ v[(src,dst)] for src, dst in queries]
