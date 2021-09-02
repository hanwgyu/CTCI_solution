# 총 가짓수는 2^N인데, 어떻게 줄일까?

# DP (i, j) 각 손가락이 마지막으로 쓴 위치에 대한 최소 distance를 저장.

class Solution:
    def minimumDistance(self, word: str) -> int:
        def distance(i: str, j: str) -> int:
            if i == -1 or j == -1:
                return 0
            x1, y1 = divmod(ord(word[i])-ord('A'), 6)
            x2, y2 = divmod(ord(word[j])-ord('A'), 6)
            return abs(x1-x2) + abs(y1-y2)

        N = len(word)
        dp = defaultdict(int) # Key : (손가락 1, 손가락 2)

        for i in range(1, N): # 현재 손가락 위치
            # 다른 손가락을 직전에 사용
            dp[(i, i-1)] = min(dp[(j, i-1)] + distance(j, i) for j in range(-1, i-1))
            dp[(i-1, i)] = min(dp[(i-1, j)] + distance(j, i) for j in range(-1, i-1))
            # 현재 손가락을 직전에 사용
            for j in range(-1, i-1):
                dp[(i, j)] = dp[(i-1, j)] + distance(i, i-1)
                dp[(j, i)] = dp[(j, i-1)] + distance(i-1, i)
        return min(min(dp[(i, N-1)] for i in range(-1, N-1)), min(dp[(N-1, i)] for i in range(-1, N-1)))
