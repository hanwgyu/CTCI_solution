# 스도쿠 문제 풀기! 답은 하나밖에 없다함.

# 걍 겁나 시도하면서 푸는 방법 밖엔 없지 않나?
# 모든 후보를 만든 후에 가장 적은 후보부터 반복해가면서?

# REMIND: backtracking 기본문제.. 근데 못풀었다. 

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None: # in-place
        """
            정말로 그냥 다해보는 방법..
        """
        def find_unsolved() -> Tuple[int, int]:
            for j in range(9):
                for i in range(9):
                    if board[i][j] == ".":
                        return (i,j)
            return (-1,-1)
    
        def check_available(i, j, e):
            for j_ in range(9):
                if board[i][j_] == e:
                    return False
            for i_ in range(9):
                if board[i_][j] == e:
                    return False
            area_i = i-i%3
            area_j = j-j%3
            for j_ in range(area_j, area_j+3):
                for i_ in range(area_i, area_i+3):
                    if board[i_][j_] == e:
                        return False
            return True
    
        def solve():
            i,j  = find_unsolved()
            if (i,j) == (-1,-1):
                return True
            for e in range(1,10):
                if check_available(i,j,str(e)):
                    board[i][j] = str(e)
                    if solve():
                        return True
                    board[i][j] = "."
            return False
    
        solve()