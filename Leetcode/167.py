class Solution:
    def twoSum(self, A: List[int], target: int) -> List[int]:
        """
        Two pointer로 풀기.
        Sorting 된 Array에서는 아래와 같이 Two pointer로 합을 구할 수 있다.
        """
        N = len(A)
        l, r = 0, N-1
        while l <= r:
            s = A[l]+A[r]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return [l+1,r+1]