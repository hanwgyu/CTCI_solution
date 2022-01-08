# 현재 위치에서 end 순으로 sorting해 가장 큰 것을 리턴.

# REMIND :  merge된 범위를 벗어나면 지금까지 나왔던 범위중에 가장 긴 범위를 더해서 업데이트 하는 방식이다. 
# 이걸 되게 깔끔하게 잘 짜면 아래와 같은 풀이가 됨.

class Solution:
    def videoStitching_1(self, clips, T):
        """
            pivot : merge된 범위의 이전 end. 
            end : 여러 범위들의 가장 오른쪽 값.
        """
        pivot, end, res = -1, 0, 0
        for i, j in sorted(clips):
            if end >= T or i > end:
                break
            elif pivot < i:
                res, pivot = res + 1, end
            end = max(end, j)
        return res if end >= T else -1 
    
    
    def videoStitching(self, clips, T):
        """
            start 가 작은 순서대로 sorting을 먼저해야 DP를 앞에서부터 진행할 수 있다.
            DP[i] 는 0~i 까지 만들기 위한 최소한의 clip 개수
        """
        dp = [float('inf')] * (101)
        dp[0] = 0
        for start, end in sorted(clips):
            for i in range(start, end+1):
                dp[i] = min(dp[i], dp[start]+1)
        return dp[T] if dp[T] != float('inf') else -1
    