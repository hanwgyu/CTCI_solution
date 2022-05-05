class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        한 줄을 더해놓고, 그로부터 오른쪽으로 이동하게 heap을 구현

        O(klogk) / O(k)
        """
        minheap = []
        M, N = len(matrix), len(matrix[0])
        for r in range(min(k, M)):
            heapq.heappush(minheap, (matrix[r][0], r, 0))
        
        for i in range(k):
            ans, r, c = heapq.heappop(minheap)
            if c+1 < N:
                heapq.heappush(minheap, (matrix[r][c+1], r, c+1))
        return ans


    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Binary Search 로 최대 범위의 값을 이동해나아가면서 그 값이 몇번째인지 매번 계산
        
        O((M+N)logD) / O(1)
        """
        M, N = len(matrix), len(matrix[0])
        
        def count(x):
            """
            x가 몇번째인지 확인.
            """
            cnt = 0
            c = N-1
            for r in range(M):
                while c>=0 and matrix[r][c] > x:
                    c -= 1
                cnt += (c+1)
            return cnt
        
        ans = 0
        l, r = matrix[0][0], matrix[-1][-1]
        while l <= r:
            m = (l+r)//2
            cnt = count(m)
            if cnt >= k:
                ans = m
                r = m-1
            else:
                l = m+1
        return ans
