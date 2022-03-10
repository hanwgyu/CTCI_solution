# 문제 설명 : 왼쪽과 오른쪽에서 숫자를 하나씩 뺴서 x를 만든다.
# 최소의 갯수를 구할 것.

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:    
        """
        Sliding Window
        
        O(N) / O(1)
        """
        N = len(nums)
        s, l, ans = sum(nums), 1, float('inf')
        nums.insert(0,0)
        for r in range(N+1):
            s -= nums[r]
            while l < r and s < x:
                s += nums[l]
                l += 1
            if s == x:
                ans = min(ans, l-1+N-r)
        return ans if ans != float('inf') else -1
                
        
    
    def minOperations1(self, nums: List[int], x: int) -> int:
        """
        Prefix Sum
        왼쪽의 합을 미리 저장해놓고, 오른쪽에서 시작해서 최소의 길이를 구함.
        
        O(N) / O(N)
        """
        N = len(nums)
        d = {0:-1}
        s = 0
        for i, n in enumerate(nums):
            s += n
            d[s] = i
        
        ans, s = float('inf'), 0
        nums.append(0)
        for i in reversed(range(N+1)):
            s += nums[i]
            if x-s in d and d[x-s]+1+N-i <= N:
                ans = min(ans, d[x-s]+1+N-i)
        return ans if ans != float('inf') else -1
            
        