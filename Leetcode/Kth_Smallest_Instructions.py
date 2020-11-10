# Solution 1 : 맨 앞자리부터 H를 놨을때 그 뒤의 총 경우의 수를 계산해 H를 놓을지 V를 놓을지 결정해나아감.
# Time : O(N), Space : O(1)

from math import comb


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        v, h = destination
        ans = []
        for _ in range(v + h):
            n = comb(h + v - 1, max(0, h - 1))
            if h == 0 or (k > n and v > 0):
                v -= 1
                k -= n
                ans.append("V")
            else:
                h -= 1
                ans.append("H")
        return "".join(ans)
