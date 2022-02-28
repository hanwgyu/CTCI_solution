class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        O(logMN) / O(1)
        """
        M, N = len(matrix), len(matrix[0])
        l, r = 0, M*N-1
        while l <= r:
            m = (l+r) // 2
            i, j = divmod(m, N)
            if matrix[i][j] > target:
                r = m-1
            elif matrix[i][j] < target:
                l = m+1
            else:
                return True
        return False