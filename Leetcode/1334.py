class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """
        Floyd-Warshall

        O(N^3) / O(N^2)
        """
    
        costs = defaultdict(lambda:float('inf'))
        for i in range(n):
            costs[(i,i)] = 0
        for i, j, cost in edges:
            costs[(i,j)] = cost
            costs[(j,i)] = cost
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    costs[(i,j)] = min(costs[(i,j)],  costs[(i,k)]+costs[(k,j)])
                    
        ans = 0
        min_cnt = float('inf')
        for i in range(n):
            cnt = sum(1 for j in range(n) if i != j and costs[(i,j)] <= distanceThreshold)
            if cnt <= min_cnt:
                min_cnt = cnt
                ans = i
        return ans
