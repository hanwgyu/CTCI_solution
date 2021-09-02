# connections의 갯수가 n-1개. loop가 없다.
# 0부터 시작해서 dfs로 뻗어나가면서 0쪽으로 향하도록 바꾸면 됨.

# 풀이 2: 좀더 깔끔하게.

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        d = defaultdict(list)
        e = set()
        for src, dst in connections:
            d[src].append(dst)
            d[dst].append(src)
            e.add((src, dst))

        def dfs(src: int, parent: int) -> int:
            return ((parent, src) in e) + sum(dfs(dst, src) for dst in d[src] if dst != parent)
        return dfs(0, -1)

    def minReorder_1(self, n: int, connections: List[List[int]]) -> int:
        src_dst, dst_src = defaultdict(list), defaultdict(list)
        for src, dst in connections:
            src_dst[src].append(dst)
            dst_src[dst].append(src)

        visited = set()
        def dfs(node: int) -> int:
            if node in visited:
                return 0
            visited.add(node)
            ans = 0
            for s in src_dst[node]:
                if s not in visited:
                    ans += 1
            return ans + sum(dfs(s) for s in src_dst[node]) + sum(dfs(s) for s in dst_src[node])
        return dfs(0)
