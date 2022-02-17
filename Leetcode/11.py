class Solution:
    def maxArea(self, A: List[int]) -> int:
        """
        Two pointer로 이동하면서, 안쪽으로 올때는 높이가 더 높아져야함.
        높이가 낮았던 쪽을 업데이트해나아감
        
        O(N) / O(1)
        """
        l, r = 0, len(A)-1
        res = 0
        while l < r:
            res = max(res, (r-l)*min(A[l],A[r]))
            if A[l] < A[r]:
                l += 1
            else:
                r -= 1
        return res