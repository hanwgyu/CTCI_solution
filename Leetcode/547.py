class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        """
        dfs
        
        O(N^2) / O(N)
        """
        visited = set()
        N = len(A)
    
        def dfs(i: int) -> int:
            if i in visited:
                return 0
            visited.add(i)
            for j in range(N):
                if A[i][j] == 1:
                    dfs(j)
            return 1
        
        return sum(dfs(i) for i in range(N))
        
        
    
    def findCircleNum1(self, A: List[List[int]]) -> int:
        """
        Union-Find. 최적화 두가지 방법을 아는게 중요!!!!!
        
        O(N^2 * logN) / O(N)
        """
        d = defaultdict(int) # key: city id(0 ~ N-1), value: province id (0~ N-1)
        N = len(A)
        for i in range(N):
            d[i] = i
        L = [0] * N # Union by rank 최적화를 위한 길이 저장

        def union(c1: int, c2: int):
            p1, p2 = find(c1), find(c2)
            if p1 != p2:
                """
                Union by rank 최적화 : https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3879/
                """
                if L[p1] > L[p2]:
                    d[p2] = p1
                elif L[p1] == L[p2]:
                    # 사실상 길이가 같을때만 업데이트 된다. 한쪽이 더 길때는 긴 길이가 유지되기 때문.
                    L[p2] += 1
                    d[p1] = p2
                else:
                    d[p1] = p2

        def find(c: int) -> int:
            """
            O(N) -> O(logN) (Union by rank) -> O(1) (Path compression)
            """
            if c1 == d[c]:
                return c
            """
            Path Compression. 단 한줄이면 된다. https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3880/
            """
            d[c] = find(d[c])
            return d[c]

        for j in range(N):
            for i in range(j):
                if A[i][j] == 1:
                    union(i, j)
        s = set()
        for i in range(N):
            s.add(find(d[i]))
        return len(s)        
