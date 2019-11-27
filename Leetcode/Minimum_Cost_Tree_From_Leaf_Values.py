# Burst Balloons 문제와 상당히 유사함.
# Solution : DP + Merge. 반씩 잘라가면서 트리의 왼쪽 오른쪽으로 나누고 각 트리의 최소합과 최대 leaf node을 리턴
# Time : O(N^2), Space : O(N^2) (DP없으면 O(N^3)?, O(N))

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        def findMinSum(l: int, r: int) -> int:
            if r-l == 1:
                return (0, arr[l])
            if (l,r) in dp:
                return dp[(l,r)]
            ret = float('inf')
            leaf_max = 0
            for i in range(l+1, r):
                (l_sum, l_max) = findMinSum(l, i)
                (r_sum, r_max) = findMinSum(i, r)
                ret = min(ret, l_sum + r_sum + l_max*r_max)
                leaf_max = max(l_max, r_max)
            dp[(l,r)] = (ret, leaf_max)
            return (ret, leaf_max)
        dp = {}
        return findMinSum(0, len(arr))[0]
