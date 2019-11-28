from collections import deque
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isPossible(cols: List[int], cur_row: int, cur_col: int) -> bool:
            for row, col in enumerate(cols):
                if cur_row == row or cur_col == col or cur_row-cur_col == row-col or cur_row+cur_col == row+col:
                    return False
            return True    
        def findAllCases(cols: List[int], cur_row: int, n: int) -> List[List[str]]:
            if cur_row == n:
                return None
            ret = deque()
            for col in range(n):
                if isPossible(cols, cur_row, col):
                    if cur_row == n-1:
                        ret.append(deque(["."*col + "Q" + "."*(n-1-col)]))
                    tmp = findAllCases(cols+[col], cur_row+1, n)
                    if tmp:
                        for e in tmp:
                            e.appendleft("."*col + "Q" + "."*(n-1-col))
                            ret.append(e)
            return ret
        return findAllCases([], 0, n)
