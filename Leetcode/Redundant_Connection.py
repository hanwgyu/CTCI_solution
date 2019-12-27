# Solution : Union-find. 같은 집합에 속한 edge가 나오면 해당 edge를 리턴.
# Time : O(N), Space: O(N)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(idx: int) -> int:
            if d[idx] != idx:
                return find(d[idx])
            return idx
        d = {i : i for i in range(len(edges)+1)}
        for e in edges:
            s0, s1 = find(e[0]), find(e[1])
            if s0 != s1:
                d[s0] = s1 
            else:
                return e
        return None
