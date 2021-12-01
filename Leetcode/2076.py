# Union-find 모든 경우에 대해 Check.
# [POINT] find 시 depth를 1로 변경해 Union시 트리의 depth가 깊어지지 않게 구현.

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = {i: i for i in range(n)}
        
        def find_and_balancing(i):
            if i != uf[i]:
                # 최종 find 결과를 저장함. (depth를 1로 변경.)
                uf[i] = find_and_balancing(uf[i])
            return uf[i]
    
        res = []
        for i, j in requests:
            success = True
            gi, gj = find_and_balancing(i), find_and_balancing(j)
            if gi != gj:
                for x,y in restrictions:
                    gx, gy = find_and_balancing(x), find_and_balancing(y)
                    if (gx, gy) == (gi, gj) or (gx, gy) == (gj, gi):
                        success = False
                        break
            if success:
                uf[gi] = gj
            res.append(success)
        return res