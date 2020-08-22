# Solution : 첫 iter에서 가장 바깥쪽 Col, row에 zero임을 표시해놓고, 두번째 iter에서
# zero임이 표시되었으면 해당 원소를 0으로 변경.
#  Time : O(MN), Space : O(1)


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_c, zero_r = False, False
        M, N = len(matrix), len(matrix[0])

        for i in range(M):
            if matrix[i][0] == 0:
                zero_c = True
                break
        for j in range(N):
            if matrix[0][j] == 0:
                zero_r = True
                break

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0

        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if zero_c:
            for i in range(M):
                matrix[i][0] = 0
        if zero_r:
            for j in range(N):
                matrix[0][j] = 0
