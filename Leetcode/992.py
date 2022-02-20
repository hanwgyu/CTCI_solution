class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        Sliding windowd인데 jump는 안됨.
        
        ㅋ.ㅋ
        ㅋ.ㅋ.ㅋ.ㅋ  매우 천재적이네!
        REMIND : exactly k = (0~k) - (0~k-1)
        
        (0~k) 인 갯수구하기
            i 이동시 그 사이에 subarray들은 모두 조건을 만족하므로, 쉽게 계산할 수 있다.
            길이가 m인 array의 모든 subarray 갯수는 m + m-2 + ... + 1 = m*(m+1)/2
        """
        def solve(nums, k:int) -> int:
            i = ans = 0
            d = defaultdict(int)
            for j, n in enumerate(nums):
                if d[n] == 0: k -= 1
                d[n] += 1
                while k < 0:
                    d[nums[i]] -= 1
                    if d[nums[i]] == 0: k += 1
                    i += 1
                ans += j-i+1
            return ans
        return solve(nums, k) - solve(nums, k-1)
