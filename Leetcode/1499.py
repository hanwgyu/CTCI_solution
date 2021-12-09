class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """
        yi + yj + |xi - xj| = (yi - xi) + (yj + xj)

        stack를 쓰면서 yi - xi 값을 작아지는 값만 저장해나아가고, 큰값은 이전값들을 덮어버림.
        비교는 맨앞에 값과만 비교함.
        # O(N) / O(N)

        REMIND: Trapping rain water 방법을 쓰는 문제.
        """
        N = len(points)
        ans = float('-inf')
        q = deque()  # (yi-xi, xi)
        for xj, yj in points:
            # 조건에 맞지않는 값들을 뺌 (xj - xi <= k)
            while q and xj - q[0][1] > k:
                q.popleft()
            if q:
                ans = max(ans, q[0][0] + yj + xj)

            # 새로운 값을 저장
            while q and q[-1][0] < yj-xj:
                q.pop()
            q.append((yj-xj, xj))
        return ans

    def findMaxValueOfEquation_1(self, points: List[List[int]], k: int) -> int:
        """
        hard인데. 당연히 시간초과
        O(N^2) / O(1)
        """
        ans = float('-inf')
        N = len(points)
        for i in range(N):
            for j in range(i+1, N):
                d = abs(points[i][0] - points[j][0])
                if d <= k:
                    ans = max(ans, points[i][1]+points[j][1]+d)
                else:
                    break
        return ans
