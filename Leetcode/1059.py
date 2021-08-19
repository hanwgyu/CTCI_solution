# 고민 1:  그래프 만들고 dfs 돌림. 한번 갔던길은 visited로 표시해서 loop가 생기는 것을 체크

# 고민 2 : 방문한 노드 목록을 복사할 필요가 없음.

# 고민 3 : 방문한 노드를 1,0,-1로 표시하면 -1은 사이클, 0은 방문 아예 안한노드, 1은 방문했고 성공한 노드로 표시가능. 전체를 순회하지 않고 time을 줄일수 있다. 매우 똑똑함.

class Solution:
    def leadsToDestination_3(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(src, dst, visited) -> bool:
            if visited[src] == -1:
                return False
            elif visited[src] == 1:
                return True
            elif not d[src]:
                return True if dst == src else False
            visited[src] = -1
            for new_src in d[src]:
                if not dfs(new_src, dst, visited):
                    return False
            visited[src] = 1
            return True

        d = defaultdict(list)
        for src, dst in edges:
            d[src].append(dst)
        return dfs(source, destination, defaultdict(int))


    def leadsToDestination_2(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(src, dst, visited) -> bool:
            if src in visited:
                return False
            if not d[src]:
                return True if dst == src else False
            visited.add(src)
            for new_src in d[src]:
                if not dfs(new_src, dst, visited):
                    return False
            visited.remove(src)
            return True

        d = defaultdict(list)
        for src, dst in edges:
            d[src].append(dst)
        return dfs(source, destination, set())

    def leadsToDestination_1(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(src, dst, visited) -> bool:
            if src in visited:
                return False
            visited.add(src)
            if not d[src]:
                return True if dst == src else False
            for new_src in d[src]:
                if not dfs(new_src, dst, visited.copy()):
                    return False
            return True

        d = defaultdict(list)
        for src, dst in edges:
            d[src].append(dst)
        return dfs(source, destination, set())
