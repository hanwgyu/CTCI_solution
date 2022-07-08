# Time : O(NlogN), Space : O(N)

# Rolling hash와 Rabin Karp 알고리즘

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def rabin_karp(L: int, a: int, mod: int, nums: List[int]) -> int:
            """
            find substring with length L
            return : start index of substring
            """
            val = 0
            for i in range(L):
                val = (val * a + nums[i]) % mod
            seen = {val}    
            
            aL = pow(a, L, mod)
            for j in range(1, len(nums)-L+1):
                # Compute rolling hash in O(1) time
                val = (a * val - nums[j-1] * aL + nums[j+L-1]) % mod
                if val in seen:
                    return j
                seen.add(val)
            return -1
        
        nums = [ord(c) - ord('a') for c in s]
        
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        mod = 2**63 - 1
        
        l, r = 1, len(s)
        # find longest length using binary search
        # 모든 길이를 다 확인하지 않고, 특정 길이가 가능하면 그것보다 짧은 길이는 항상 조건을 만족하므로, binary search를 적용할 수 있다.
        # binary search index 계산하는 과정이 어려움. 외워야 하는듯?
        start = 0
        while l <= r:
            m = (l+r)//2
            i = rabin_karp(m, a, mod, nums)
            if i != -1:
                l = m + 1
                start = i
            else:
                r = m - 1
        return s[start:start+l-1]
