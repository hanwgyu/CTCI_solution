# 문제 설명: sum(left) < sum(mid) < sum(right) 세 subarray로 나누는 방법의 수

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        """
        1번 방법을 two pointer 문제로 풀어서 계산량을 줄임.
        
        i를 키우면 l이 커지고, m이 작아짐.
        j를 키우면 m이 커지고, r이 작아짐.
        
        i를 키우면서 j의 범위 f, t을 구함
        i를 키우면 f를 키워야만 하고, t도 더 커질 수 있다.
        O(N) / O(N)
        """
        N = len(nums)
        sums = list(accumulate(nums))
        ans = 0
        f,t = 0, 0
        for i in range(N-2):
            while f <= i or (f < N-1 and sums[i] > sums[f] - sums[i]):
                f += 1
            while t < f or (t < N-1 and sums[t] - sums[i] <= sums[-1] - sums[t]):
                t += 1
            ans = (ans+t-f) % (10**9+7)
        return ans
    
    def waysToSplit1(self, nums: List[int]) -> int:
        """
        Prefix sum으로 2개의 포인트를 결정하면 됨.
        sum 이 점점 커지도록.
        
        O(N^2) / O(N)
        """
        sums = [0]
        s, N = 0, len(nums)
        for n in nums:
            s += n
            sums.append(s)
        ans = 0
        for i in range(N):
            for j in range(i+1, N):
                l, m, r = sums[i+1] - sums[0], sums[j+1] - sums[i+1], sums[-1] - sums[j+1]
                if l <= m <= r:
                    ans += 1
                if sums[i+1] > r:
                    break
        return ans % (10**9+7)