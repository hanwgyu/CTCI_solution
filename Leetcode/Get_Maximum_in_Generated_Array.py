# Time : O(N), Space: O(N)

from collections import deque
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        q = deque([1])
        ans, a = 0, 0
        for i in range(2,n+1):
            if i % 2 == 0:
                a = q.popleft()
                q.append(a)
                ans = max(ans, a)
            else:
                q.append(a+q[0])
                ans = max(ans, a+q[0])
        return ans
    
    
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        a = [0, 1]
        for i in range(2, n + 1):
            a.append(a[i // 2] if i % 2 == 0 else a[i // 2] + a[i // 2 + 1])
        return max(a)
