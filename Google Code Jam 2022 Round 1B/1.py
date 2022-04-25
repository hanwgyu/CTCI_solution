import math

from collections import defaultdict


def solution():
    def solve():
        """
        array의 특정 위치에서 끝나는 경우를 생각하면, 왼쪽에서 쭉 오고, 오른쪽에서 쭉 오는게 베스트.

        O(N) / O(N)
        """
        num_cakes = input()
        A = list(map(int, input().split()))
        N = len(A)

        l, r = [0 for _ in range(N+1)], [0 for _ in range(N+1)]
        ans, m = 0, 0
        for i in range(N):
            if A[i] >= m:
                ans = ans+1
                m = A[i]
            l[i+1] = ans
        ans, m = 0, 0
        for i in reversed(range(N)):
            if A[i] >= m:
                ans = ans+1
                m = A[i]
            r[i] = ans
        return max(l[i]+r[i] for i in range(N+1))

    def solve():
        """
        Two pointers. 작은 값을 만났을때 이동한다.

        O(N) / O(1)
        """
        num_cakes = input()
        A = list(map(int, input().split()))
        N = len(A)

        ans = 0
        maxn = 0
        l, r = 0, N-1
        while l <= r:
            if A[l] < A[r]:
                a = A[l]
                l += 1
            else:
                a = A[r]
                r -= 1
            ans = ans+1 if a>=maxn else ans
            maxn = max(maxn, a)
        return ans

    def solve():
        """
        DP.

        O(N^2) / O(N)
        """
        num_cakes = input()
        A = list(map(int, input().split()))
        N = len(A)
        
        front = (0,0) #ans, max
        ans = 0
        dp = [(0,0) for _ in range(N+1)]
        for i in range(-1, N):
            if i >= 0:
                front = (front[0] + (1 if A[i] >= front[1] else 0), max(front[1], A[i]))
                dp[N] = front
            for j in range(N-1, i, -1):
                l = (0,0)
                if i >= 0:
                    l = (dp[j][0]+ (1 if A[i] >= dp[j][1] else 0), max(dp[j][1], A[i]))
                r = (dp[j+1][0]+ (1 if A[j] >= dp[j+1][1] else 0), max(dp[j+1][1], A[j]))
                dp[j] = max(l, r, key=lambda e: (e[0], -e[1]))
            ans = max(ans, dp[j][0])
        return ans
        
    for T in range(1,1+int(input())):
        ans = solve()
        print("Case #%d:" % T, ans)       

solution()
