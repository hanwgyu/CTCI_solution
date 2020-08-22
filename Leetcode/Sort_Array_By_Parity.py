# Solution 1 :
# Time : O(N), Space : O(N)

# Solution 2 : In-place
# Time : O(N), Space : O(1)

from collections import deque


class Solution:
    def sortArrayByParity_2(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] % 2 > A[r] % 2:
                A[l], A[r] = A[r], A[l]
            if A[l] % 2 == 0:
                l += 1
            if A[r] % 2 == 1:
                r -= 1
        return A

    def sortArrayByParity_1(self, A: List[int]) -> List[int]:
        d = deque()
        for n in A:
            if n % 2 == 0:
                d.appendleft(n)
            else:
                d.append(n)
        return list(d)
