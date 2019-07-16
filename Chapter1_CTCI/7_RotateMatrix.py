#1-7 RotateMatrix
#시간 복잡도 : O(n^2)
import unittest


def function(matrix):
  n = len(matrix)

  for i in range((n+1)//2):
    for j in range(i, n-i-1):  
      temp = matrix[i][j]
      matrix[i][j] = matrix[n-1-j][i]
      matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
      matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
      matrix[j][n-1-i] = temp   

  return matrix

class Test(unittest.TestCase):
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]),
        ([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ], [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ])
    ]

    def test_function(self):
        for data in self.data:
            res = function(data[0])
            self.assertEqual(res, data[1])


if __name__ == "__main__":
    unittest.main()