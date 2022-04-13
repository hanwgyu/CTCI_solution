class Solution:
    def dailyTemperatures(self, A: List[int]) -> List[int]:
        """
        Monotonic stack

        O(N) / O(N)
        """
        N = len(A)
        ans, s = [0 for _ in range(N)],[]
        for i in reversed(range(N)):
            while s and A[i] >= A[s[-1]]:
                s.pop()
            if s:
                ans[i] = s[-1] - i
            s.append(i)
        return ans

    def dailyTemperatures(self, A: List[int]) -> List[int]:
        """
        뒤에서부터 시작하되, 결과를 저장해놓은것으로 점프를 해서 계산.
        
        O(N) / O(1)
        """
        N = len(A)
        ans = [0 for _ in range(N)]
        max_temp = 0
        for i in reversed(range(N)):
            if A[i] < max_temp:
                j = i+1
                while A[i] >= A[j]:
                    j = j+ans[j]
                ans[i] = j-i
            max_temp = max(A[i], max_temp)
        return ans
    
    