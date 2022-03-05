class Solution:
    def findMin(self, A: List[int]) -> int:
        lo, hi = 0, len(A)-1
        while lo < hi:
            mid = (lo+hi)//2
            if A[mid] > A[hi]:
                lo = mid+1
            elif A[mid] < A[hi]:
                hi = mid
            else:
                hi = hi-1
        return A[lo]