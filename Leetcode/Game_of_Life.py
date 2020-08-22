# Solution : 각 cell을 저장공간으로 사용하여, 첫번쨰 iter에서 주변 cell의 합을 10의자리에 현재 cell 값을 1의 자리에 저장.
# 두번째 iter에서 저장된 합을 이용해 값을 바꿈.
# Time : O(MN), Space : O(1)


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def getNeighborsSum(i: int, j: int):
            s = 0
            for i_ in range(i - 1, i + 2):
                for j_ in range(j - 1, j + 2):
                    s = (
                        s + board[i_][j_] % 10
                        if 0 <= i_ < self.M and 0 <= j_ < self.N
                        else s
                    )
            return s - board[i][j]

        self.M, self.N = len(board), len(board[0])

        for i in range(self.M):
            for j in range(self.N):
                board[i][j] += getNeighborsSum(i, j) * 10

        # 값이 0일때, 주변 합이 3이면 값을 변경.
        # 값이 1일때, 주변 합이 1이하이거나 4이상이면 값을 변경.
        for i in range(self.M):
            for j in range(self.N):
                s, num = board[i][j] // 10, board[i][j] % 10
                if num == 0:
                    if s == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if s <= 1 or s >= 4:
                        board[i][j] = 0
                    else:
                        board[i][j] = 1
