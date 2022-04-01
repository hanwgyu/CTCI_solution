# Solution1 : DFS
# Time : O(N), Space: O(N)

# Solution2 : Union-find. 'a == b'에 해당되는 각 노드들을 일렬(a가 parent)로 연결.
# 그 이후, 'a != b'를 체크할때 a의 root와 b의 root가 같으면 False를 리턴.
# Time : O(N), Space : O(N)

import string
from collections import defaultdict


class Solution:
    def equationsPossible_2(self, equations: List[str]) -> bool:
        def find(c: str) -> str:
            if colors[c] != c:
                return find(colors[c])
            return c

        colors = {c: c for c in string.ascii_lowercase}
        for e in equations:
            if e[1] == "=":
                colors[find(e[0])] = find(e[3])
        return not any(
            e[1] == "!" and find(e[0]) == find(e[3]) for e in equations
        )

    def equationsPossible_1(self, equations: List[str]) -> bool:
        def canMeet(src, dst, visited):
            if src == dst:
                return True
            visited[src] = True
            for a in graph[src]:
                if visited[a]:
                    continue
                if canMeet(a, dst, visited):
                    return True
            return False

        graph = defaultdict(list)
        for e in equations:
            if e[1] == "=":
                graph[e[0]].append(e[3])
                graph[e[3]].append(e[0])

        for e in equations:
            if e[1] == "!":
                if canMeet(e[0], e[3], defaultdict(lambda: False)):
                    return False
        return True


    def equationsPossible(self, equations: List[str]) -> bool:
        """
        graph. Union-Find
        
        depth를 줄이기 위해 짧은 depth를 가진 쪽을 긴쪽에 연결
        """
        d = defaultdict(str)
        for src, _, _, dst  in equations:
            d[src] = [src, 1]
            d[dst] = [dst, 1]
        
        def find(src: str) -> str:
            return src if d[src][0] == src else find(d[src][0])
            
        def union(src: str, dst: str):
            a, b = d[find(src)], d[find(dst)]
            if a[0] == b[0]:
                return
            if a[1] > b[1]:
                d[b[0]] = a[0]
                d[a[0]][1] += 1
            else:
                d[a[0]] = b[0]
                d[b[0]][1] += 1
        
        st = []
        for src, eq, _, dst  in equations:
            eq = True if eq == "=" else False
            if eq:
                union(src, dst)
            else:
                st.append((src, dst))
        return all(find(src) != find(dst) for src, dst in st)