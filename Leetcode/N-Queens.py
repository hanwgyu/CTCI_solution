# Solution 2 : Sol 1에 cols 공유하도록 변경. 복사비용 줄임. O(N!) / O(N)

from collections import deque
class Solution:
    def solveNQueens_2(self, n: int) -> List[List[str]]:
        def isPossible(cur_row: int) -> bool:
            for row in range(cur_row):
                if abs(cols[cur_row]-cols[row]) == abs(cur_row-row) or cols[cur_row] == cols[row]:
                    return False
            return True
        
        def addSolution():
            tmp = []
            for row in range(n):
                col = cols[row]
                tmp.append("."*col + "Q" + "."*(n-1-col))
            ans.append(tmp)
        
        def findAllCases(cur_row: int):
            if cur_row == n:
                addSolution()
                return
            for col in range(n):
                cols[cur_row] = col
                if isPossible(cur_row):
                    findAllCases(cur_row+1)            
        cols, ans = [0] * n, []
        findAllCases(0)
        return ans
  
#############################################################################################    
    def solveNQueens_1(self, n: int) -> List[List[str]]:
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
