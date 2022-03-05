# 문제 설명 : 합이 K 이상인 subarray 의 가장 짧은 길이 구하기.

from collections import deque
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        """
        Prefix Sum을 저장해나아가는데, stack에 저장함.
        점점 커지게 값을 저장.
        앞에서부터 비교해서 정답을 업데이트하고, pop한다. (이게 중요, 최소 길이이므로 다시계산할 필요 없다.) 
        O(N) / O(N)
        """
        deq = deque([(0, -1)])
        ans = float('inf')
        s = 0
        for i, a in enumerate(A):
            s += a
            while deq and s - deq[0][0] >= K:
                ans = min(ans,  i-deq[0][1])
                deq.popleft()
            while deq and deq[-1][0] > s:
                deq.pop()
            deq.append((s, i))
        return ans if ans != float('inf') else -1   