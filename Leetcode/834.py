"""
현재 노드로부터 다른 모든 노드로까지의 거리의 합을 구할것.

모든 노드에서 dfs로 돌면 O(N^2)으로 풀수있으나 더 줄일수 있음.

dfs로 돌면서 그 아래쪽으로의 노드 갯수를 저장하고, dfs 시작점은 온전한 결과값이라는걸 이용해 
두 노드에서의 차이 값을 이용해 계산.

O(N) / O(N)
"""

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        count = [1 for _ in range(n)]
        res = [0 for _ in range(n)]
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
            
        # 특정 위치로부터 dfs로 돌면서 count(각 노드에 연결된 child 갯수)를 저장하면서
        # child tree로부터의 결과를 저장함
        def postorder(src: int, visited = set()):
            if src in visited:
                return
            visited.add(src)
            for dst in adj_list[src]:
                if dst not in visited:
                    postorder(dst, visited)
                    count[src] += count[dst]
                    res[src] += res[dst] + count[dst]
        postorder(edges[0][0])
    
        # 시작 지점이 정답이고, 동일한 방향으로 dfs로 돌면서
        # (res[parent] - (res[child]+count[child])) + (n-count[child]): child 에서 parent 쪽으로의 비용
        def preorder(src: int, visited = set()):
            if src in visited:
                return
            visited.add(src)
            for dst in adj_list[src]:
                if dst not in visited:
                    res[dst] += res[src] - (res[dst]+count[dst]) + n - count[dst]
                    preorder(dst, visited)
        preorder(edges[0][0])
        return res
