class Solution:
    def findMin2(self, A: List[int]) -> int:
        lo, hi = 0, len(A)-1
        while lo < hi:
            mid = (lo+hi)//2
            if A[mid] > A[hi]:
                lo = mid+1
            else:
                hi = mid
        return A[lo]
    
    def findMin1(self, A: List[int]) -> int:
        N = len(A)
        l, r = 0, N-1
        while l <= r:
            m = (l+r)//2
            if A[l] <= A[m] <= A[r]:
                return A[l]
            if A[m-1] > A[m]:
                return A[m]
            if A[l] <= A[m]:
                l = m+1
            else:
                r = m-1
        return -1