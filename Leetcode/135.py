# 문제 설명: 캔디를 한개 이상씩 주고, rating이 양옆 사람보다 큰 경우 캔디를 더줘야한다.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        1부터 시작, 양쪽에서 시작해서, 커질때만 1을 키워서 저장.
        
        O(N) / O(N)
        """
        N = len(ratings)
        res = N * [1]
        for i in range(1, N):
            if ratings[i-1] < ratings[i]:
                res[i] = max(res[i], res[i-1] + 1)
        for i in reversed(range(1, N)):
            if ratings[i-1] > ratings[i]:
                res[i-1] = max(res[i-1], res[i] + 1) 
        return sum(res)