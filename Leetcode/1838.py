class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        diff를 거꾸로 prefix sum으로 저장하여 가장 길고 k값을 넘기는 값을 찾음
        Sliding window
        ex) 5 4 2 1
        diff : 1 3 4
        
        O(NlogN) / O(1)
        """
        N = len(nums)
        nums.sort(reverse=True)
        j, s, ans = 0, 0, 1
        for i in range(N-1):
            while j < N and s + nums[i]-nums[j] <= k:
                s += nums[i]-nums[j]
                j += 1
            s -= (j-i-1)*(nums[i]-nums[i+1])
            ans = max(ans, j-i)
        return ans