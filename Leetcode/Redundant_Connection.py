# Solution 1 : Union-find. 같은 집합에 속한 edge가 나오면 해당 edge를 리턴.
# Time : O(N^2), Space: O(N)

# Solution 2 : Optimized Union-find.
# Time : O(N), Space: O(N)


class Solution:
    def findRedundantConnection_2(self, edges: List[List[int]]) -> List[int]:
        def find(idx: int) -> int:
            if d[idx] != idx:
                # Tree 구조를 height 1로 만들기 위한 방법!!!!
                d[idx] = find(d[idx])
                return d[idx]
            return idx

        def union(x: int, y: int) -> bool:
            if x == y:
                return False
            if depth[x] < depth[y]:
                d[x] = y
            elif depth[x] > depth[y]:
                d[y] = x
            else:
                d[y] = x
                depth[y] += 1
            return True

        d = {i: i for i in range(len(edges) + 1)}
        depth = {i: 0 for i in range(len(edges) + 1)}
        for e in edges:
            if not union(find(e[0]), find(e[1])):
                return e
        return None

    def findRedundantConnection_1(self, edges: List[List[int]]) -> List[int]:
        def find(idx: int) -> int:
            if d[idx] != idx:
                return find(d[idx])
            return idx

        d = {i: i for i in range(len(edges) + 1)}
        for e in edges:
            s0, s1 = find(e[0]), find(e[1])
            if s0 != s1:
                d[s0] = s1
            else:
                return e
        return None

    
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        DFS. 위의 union-find가 더 효율적.
        """
        adj_list = defaultdict(list)
        
        def is_connected(src, dst):
            if src == dst:
                return True
            for mid in adj_list[src]:
                if mid not in visited:
                    visited.add(mid)
                    if is_connected(mid, dst):
                        return True
            return False
        
        for src, dst in edges:
            visited = set()
            if is_connected(src,dst):
                return [src, dst]
            adj_list[src].append(dst)
            adj_list[dst].append(src)
