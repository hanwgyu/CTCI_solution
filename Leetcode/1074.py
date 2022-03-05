class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        Prefix Sum
        
        Prefix Sum으로 row의 누적 합을 저장해놓고,
        두번째로 다시 Prefix Sum을 사용해 rows[i:j+1] 범위의 column들의 누적 합을 저장해나아가면서 개수를 계산.
        
        O(MN^2) / O(M)
        """
        M, N = len(matrix), len(matrix[0])
        for rows in matrix:
            for i in range(1, N):
                rows[i] += rows[i-1]
        
        ans = 0
        for i in range(N+1):
            for j in range(i+1, N+1):
                d = defaultdict(int)
                d[0] = 1
                s = 0
                for rows in matrix:
                    s += rows[j-1]-rows[i-1] if i > 0 else rows[j-1]
                    ans += d[s-target]
                    d[s] += 1
        return ans
                    