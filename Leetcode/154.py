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

class Solution:
    def findMin(self, A: List[int]) -> int:
        l, r = 0, len(A)-1
        while l <= r:
            m = (l+r)//2
            # 원소가 겹칠때만 예외처리. 모든 케이스를 계산하도록 해준다.
            # [6,1,6,6,6,6,6]이나 [6,6,6,6,6,1,6] 두 케이스에서 오른쪽이나 왼쪽 중 어디로 갈지 알수없기 때문.
            if A[l] == A[m] == A[r]:
                r = r-1
                continue
            # 아랫 부분은 겹치는 원소가 없는 'Find Minimum in Rotated Sorted Array' 문제와 동일하다.
            if m > 0 and A[m-1] > A[m]:
                return A[m]
            if A[m] < A[r]:
                r = m-1
            elif A[m] > A[r]:
                l = m+1
            else:
                r = m-1
        return A[l]
    """
    l = r =m 인 상황을 고려한 조건문을 하나로 합치면 아래와 같이 된다.
    """
    def findMin(self, A: List[int]) -> int:
        l, r = 0, len(A)-1
        while l <= r:
            m = (l+r)//2
            if m > 0 and A[m-1] > A[m]:
                return A[m]
            if A[m] < A[r]:
                r = m-1
            elif A[m] > A[r]:
                l = m+1
            else:
                r = r-1
        return A[l]
