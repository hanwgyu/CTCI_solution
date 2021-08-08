# 고민 1 : DP.
# 각 column에 해당하는 값을 저장해가면서 다음 row로 넘어감.
# Time : O(MN^2), Space : O(N)

# 고민 2 : DP. 계산 시간 줄여보기
# [a,b,c,d]
# l : [max(a-3, b-2, c-1, d), max(b-2, c-1, d), max(c-1, d), d]
# r : [a, max(a, b-1), max(a, b-1, c-2), max(a, b-1, c-2, d-3)]
# Time : O(MN), Space : O(N)

# 고민 3 : DP. 계산 시간 줄여보기
# 더 압축해서 저장해놓는 방법. 미리 max를 구함.
# Time : O(MN), Space : O(N)


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n_cols = len(points[0])
        dp = [0] * n_cols
        for row in points:
            for i in range(1, n_cols):
                dp[i] = max(dp[i], dp[i - 1] - 1)
                dp[-i - 1] = max(dp[-i - 1], dp[-i] - 1)
            for i, col in enumerate(row):
                dp[i] += col
        return max(dp)

    def maxPoints_2(self, points: List[List[int]]) -> int:
        def right(dp: List[int]) -> List[int]:
            # i번째 원소는 i부터 마지막까지 내에서 max값을 리턴. max(ai-i, ..., an-n)
            ret = [0] * (len(dp)-1) + [dp[-1]-(len(dp)-1)]
            for i in reversed(range(0, len(dp)-1)):
                ret[i] = max(ret[i+1], dp[i]-i)
            return ret
        def left(dp: List[int]) -> List[int]:
            # i+1번째 원소는 0부터 i번째까지 내에서 max값을 리턴. max(a0-n, ..., ai-(n-i))
            ret = [dp[0]-(len(dp)-1)] + [0] * (len(dp)-1)
            for i in range(1, len(dp)):
                ret[i] = max(ret[i-1], dp[i]-(len(dp)-1-i))
            return ret

        M, N = len(points), len(points[0])
        dp = [0 for _ in range(N)]
        dp_prev = [0 for _ in range(N)]
        for i in range(M):
            l,r = left(dp_prev), right(dp_prev)
            for j in range(N):
                dp[j] = points[i][j] + max(l[j]+len(dp)-1-j, r[j]+j)
            dp_prev = dp.copy()
        return max(dp)

    def maxPoints_1(self, points: List[List[int]]) -> int:
        M, N = len(points), len(points[0])
        dp = [0 for _ in range(N)]
        dp_prev = [0 for _ in range(N)]
        for i in range(M):
            for j in range(N):
                dp[j] = points[i][j] + max([dp_prev[k] - abs(k-j) for k in range(N)])
            dp_prev = dp.copy()
        return max(dp)
