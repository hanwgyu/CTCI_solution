# 1-8 ZeroMatrix
# 시간 복잡도 : O(MN) ,공간 복잡도 : O(M+N)
# Set으로 바꿀 것
import unittest


def function(matrix):
    m = len(matrix)
    n = len(matrix[0])
    zero_row = [False for _ in range(m)]
    zero_col = [False for _ in range(n)]

    # Check which row or column has to be zero
    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                zero_row[x] = True
                zero_col[y] = True

    # Apply to be zero
    for x in range(m):
        if zero_row[x] is True:
            for y in range(n):
                matrix[x][y] = 0

    for y in range(n):
        if zero_col[y] is True:
            for x in range(m):
                matrix[x][y] = 0

    return matrix


class Test(unittest.TestCase):
    data = [
        (
            [[1, 2, 0, 4], [5, 6, 7, 8], [0, 10, 11, 12], [13, 14, 15, 16]],
            [[0, 0, 0, 0], [0, 6, 0, 8], [0, 0, 0, 0], [0, 14, 0, 16]],
        )
    ]

    def test_function(self):
        for data in self.data:
            res = function(data[0])
            self.assertEqual(res, data[1])


if __name__ == "__main__":
    unittest.main()
