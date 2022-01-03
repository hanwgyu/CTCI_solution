# 먼저 각 사람에 대해 받거나 갚아야하는 총 금액을 계산함.
# 특정 그룹에 대해 빚을 상쇄시켜나아감. bfs로.
# 그룹안에서는 한곳으로 모이는 형태로됨. 즉, 그룹사이즈 -1 만큼의 transaction이 필요함.

# REMIND : DFS로 모든걸 도는건데 생각하는것 자체가 너무. 어려움.

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt = defaultdict(int)
        for f, t, amount in transactions:
            debt[f] -= amount
            debt[t] += amount
        debt = [i for i in debt.values() if i != 0]
        N = len(debt)
        
        def dfs(p:int) -> int:
            while p < N and debt[p] == 0: 
                p += 1
            if p == N:
                return 0
            res = float('inf')
            for i in range(p+1, N):
                if debt[i]*debt[p] < 0:
                    debt[i] += debt[p]
                    res = min(res, 1+dfs(p+1))
                    debt[i] -= debt[p]
            return res if res != float('inf') else 0
            
        return dfs(0)