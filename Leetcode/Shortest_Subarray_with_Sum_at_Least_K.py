# Solution 1 : BruteForce
# Time : O(N^2), Space : O(1)

# Solution 2 : i번째까지의 합들을 먼저 구하고, queue에 저장하되, 크기가 커지는 순으로만 저장. (현재보다 큰 원소들을 모두 제거. (가장 짧은 거리를 구해야하기 때문에 크기가 작고 가장 최근 원소를 저장하는 것이 이득.))
# 새로 원소를 추가할때 queue 가장 앞 값과 현재 원소와의 차이가 K보다 크면 가장 앞값은 제거하고 index 차이를 계산.
# Time : O(N), Space : O(N)
# 'Trapping Rain Water' 문제와 비슷

from collections import deque


class Solution:
    def shortestSubarray_2(self, A: List[int], K: int) -> int:
        q, acc = deque(), [0]
        ans = float("inf")
        for e in A:
            acc.append(acc[-1] + e)
        for i, e in enumerate(acc):
            while q and e <= acc[q[-1]]:
                q.pop()
            while q and e - acc[q[0]] >= K:
                ans = min(ans, i - q.popleft())
            q.append(i)
        return ans if ans != float("inf") else -1

    def shortestSubarray_1(self, A: List[int], K: int) -> int:
        ans = float("inf")
        for i in range(len(A)):
            s = 0
            for j in range(i, len(A)):
                s += A[j]
                if s >= K:
                    ans = min(ans, j - i + 1)
                    break
        return ans if ans != float("inf") else -1
