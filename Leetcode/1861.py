class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
        Two pointers
        
        O(MN) / O(1)
        """
        M, N = len(box), len(box[0])
        res = [['.' for _ in range(M)] for _ in range(N)]
        for i in range(M):
            k, rocks = N-1, 0
            for j in reversed(range(N)):
                if box[i][j] == "#":
                    rocks += 1
                elif box[i][j] == "*":
                    res[j][M-1-i] = "*"
                    while rocks > 0:
                        res[k][M-1-i] = "#"
                        k, rocks = k-1, rocks-1
                    k = j-1
            while rocks > 0:
                res[k][M-1-i] = "#"
                k, rocks = k-1, rocks-1     
        return res