# DP로 특정 노드에서의 horizontal, vetical, diagonal, anti-daigonal visited 여부를 저장.

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        visited = defaultdict(bool) # key : (i, j, type) (type : 0,1,2,3)
        M, N = len(mat), len(mat[0])
        types = {0: (0,1), 1: (1,0), 2: (1,1), 3: (1, -1)}
        ans = 0

        for i in range(M):
            for j in range(N):
                for type, (di, dj) in types.items():
                    ti, tj = i, j
                    if visited[(ti, tj, type)]:
                        continue
                    cnt = 0
                    while 0 <= ti < M and 0 <= tj < N:
                        visited[(ti, tj, type)] = True
                        if mat[ti][tj] == 0:
                            break
                        cnt += 1
                        ti, tj = ti+di, tj+dj
                    ans = max(ans, cnt)
        return ans

