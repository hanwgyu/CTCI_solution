# 나누기는 1를 구해야할때만 쓰임.

# Solution 1: target을 x로 나누면서 나머지가 더하거나 뺼때 작아지는 방향으로 계산.Recursive.
# maximum recursion depth exceed. Time : O(logx(target)), Space: O(logx(target))
# 작은 나머지부터 결정하기에는 불확실성이 많아서 recursion에 의한 공간 복잡도가 너무 커짐.
# DP를 추가해도 test case를 넘길만큼 속도가 안나옴.

# 2번 방법으로 큰 수부터 결정해나아가면 최적화가 가능. 1)sums-target<target 일때만 neg를 구하고 
# 2) target x차수로 정확하게 계산되면 power를 바로 리턴.

# Solution 2: target에 가까운 x차수에서 뺴거나 더하면서 나머지를 구해감. Recursive.
# Time Limit Exceed. Time : O(logx(target)), Space: O(logx(target))?

# Solution 3: Solution 1 방법을 pos, neg를 매번 갱신해가면서 처리가능.
# 1번에서 미래(더큰 차수)의 결과를 알지 못하면 현재를 결정하지 못한다고 생각하고 recursive로 짠건데 그럴 필요가 없었다.
# Time : O(logx(target)), Space: O(1)


class Solution:
    def cost(self, power : int) -> int:
        return power if power > 0 else 2
    
    def leastOpsExpressTarget_3(self, x, y):
        pos = neg = k = 0
        while y:
            y, res = divmod(y, x)
            if p:
                pos, neg = min(res * self.cost(p) + pos, (res+1) * self.cost(p) + neg), min((x-res) * self.cost(p) + pos, (x-res-1) * self.cost(p) + neg)
            else:
                pos, neg = res * self.cost(0), (x - res) * self.cost(0)
            p += 1
        return min(pos, k + neg) - 1
    
    
    def leastOpsExpressTarget_2(self, x: int, y: int) -> int:
        if x > y:
            return min(self.cost(0) * y, self.cost(0) * (x - y) + self.cost(1)) - 1        
        p, sums = 1, x
        while y > sums:
            sums *= x
            p += 1
        if y == sums:
            return self.cost(p) - 1       
        pos, neg = float('inf'), float('inf')
        if sums - y < y:
            neg = self.leastOpsExpressTarget(x, sums - y) + self.cost(p)
        pos = self.leastOpsExpressTarget(x, y - sums//x) + self.cost(p-1)
        return min(pos, neg)   
    
    
    def leastOpsExpressTarget_1(self, x: int, y: int) -> int:
        def minCost(x: int, y: int, p: int) -> int:
            if y == 0:
                return 0
            if y == 1:
                return self.cost(p)
            y, res = divmod(y, x)
            return min(minCost(x, y+1, p+1) + self.cost(p) * (x-res), minCost(x, y, p+1) + self.cost(p) * res)
        return minCost(x, y, 0) - 1
