class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        31번 문제와 동일
        O(N) / O(N)
        """
        A = list(map(int, str(n)))
        i = j = len(A)-1
        while i > 0 and A[i-1] >= A[i]:
            i -= 1
        if i == 0:
            return -1
        while A[j] <= A[i-1]:
            j -= 1
        A[i-1], A[j] = A[j], A[i-1]
        A[i:len(A)] = A[i:len(A)][::-1]
        res = int("".join(list(map(str, A))))
        return res if res < 2**31 else -1