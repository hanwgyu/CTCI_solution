# Sol 1: Time : O(MN), Space : O(1)


class Solution:
    def spiralOrder_2(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder(
            [*zip(*matrix)][::-1]
        )

    def spiralOrder_1(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        N, M, ans = len(matrix), len(matrix[0]), []
        i, j, di, dj = 0, 0, 1, 0
        for _ in range(M * N):
            ans.append(matrix[j][i])
            matrix[j][i] = 0
            if (
                (i == M - 1 and j == 0)
                or (N != 1 and i == 0 and j == N - 1)
                or (i == M - 1 and j == N - 1)
                or (matrix[j + dj][i + di] == 0)
            ):
                di, dj = -dj, di
            i += di
            j += dj
        return ans
