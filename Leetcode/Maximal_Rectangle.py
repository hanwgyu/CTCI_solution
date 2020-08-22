# Solution 1 : DP. 왼쪽방향의 연속된 1의 갯수를 저장해나아감. 매 블럭에서 최대 area를 계산.
# Time : O(MN^2), Space : O(MN)

# Solution 2: DP + Stack. 높이를 저장해나아가면서, Stack을 이용해 최대 넓이를 구해감.
# 'Trapping rain water' 문제와 비슷하게.
# Time : O(MN), Space : O(N)

# Solution 3 : Solution 2에서 index저장하는 방법을 좀더 깔끔하게.


class Solution:
    def maximalRectangle_3(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        M, N = len(matrix), len(matrix[0])
        st, dp = [(0, -1)], [0 for _ in range(N)]
        ans = 0
        for i in range(M):
            for j in range(N):
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0
                # 높이가 높아지는 것만 저장.
                while st[-1][1] != -1 and st[-1][0] >= dp[j]:
                    h = st.pop()[0]
                    ans = max(ans, h * (j - st[-1][1] - 1))
                st.append((dp[j], j))
            while st[-1][1] != -1:
                h = st.pop()[0]
                ans = max(ans, h * (N - st[-1][1] - 1))
        return ans

    def maximalRectangle_2(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        M, N = len(matrix), len(matrix[0])
        st, dp = [], [0 for _ in range(N)]
        ans = 0
        for i in range(M):
            for j in range(N):
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0
                # 높이가 높아지는 것만 저장.
                min_j = float("inf")
                while st and st[-1][0] >= dp[j]:
                    (h, start_j) = st.pop()
                    ans = max(ans, h * (j - start_j))
                    min_j = start_j
                if dp[j] > 0:
                    st.append((dp[j], min(min_j, j)))
            while st:
                (h, start_j) = st.pop()
                ans = max(ans, h * (N - start_j))
        return ans

    def maximalRectangle_1(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]
        ans = 0
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == "1":
                    dp[i][j] = dp[i][j - 1] + 1 if j > 0 else 1
                    temp_i, l = i, float("inf")
                    while temp_i >= 0 and matrix[temp_i][j] == "1":
                        l = min(l, dp[temp_i][j])
                        ans = max(ans, l * (i - temp_i + 1))
                        temp_i -= 1
        return ans
