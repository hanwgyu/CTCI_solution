class Solution:
    def findLength1(self, nums1: List[int], nums2: List[int]) -> int:
        """
        DP.
        작은 길이부터 비교해서 완료된 결과를 dp에 저장.
        dp[i][j]에 nums i, nums j 번째가 마지막인 subarray의 최대 겹치는 길이를 저장
        
        O(MN) / O(MN)
        """
        M, N = len(nums1), len(nums2)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        ans = 0
        for i in range(1, M+1):
            for j in range(1, N+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    ans = max(ans, dp[i][j])
        return ans
        
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:     
        """
        REMIND:
        1) 길이 비교를 binary search를 통해 줄인다.  
        2) 문자열 비교시 rolling hash 이용해 횟수를 줄인다.
        
        O((M+N)log(min(M,N))) / O(M+N)
        """
        BASE, MOD = 101, 10**9+7            
        M, N = len(nums1), len(nums2)
        l, r = 0, min(M, N)
        ans = 0
        # 0~i 위치까지의 hash값을 미리 구해놓는다.
        hash1, hash2, pows = [0 for _ in range(M+1)], [0 for _ in range(N+1)], [1 for _ in range(min(M, N)+1)]
        for i in range(1, min(M,N)+1): pows[i] = pows[i-1] * BASE % MOD
        for i in range(1, M+1): hash1[i] = (hash1[i-1] * BASE + nums1[i-1]) % MOD
        for i in range(1, N+1): hash2[i] = (hash2[i-1] * BASE + nums2[i-1]) % MOD
        
        def rollingHash(hash1: List[int], l: int, r: int) -> int:
            """
            위에서 구해놓은 hash값을 이용해 [l:r+1] 범위의 hash값을 구한다.
            """
            return (hash1[r+1] - hash1[l]*pows[r-l+1]%MOD ) % MOD
            
            
        def solve(length: int) -> bool:
            """
            length 길이의 겹치는 subarray가 있는지 확인
            """
            seen = defaultdict(list)
            for i in range(M-length+1):
                h = rollingHash(hash1, i, i+length-1)
                seen[h].append(i)
            for j in range(N-length+1):
                h = rollingHash(hash2, j, j+length-1)
                if h in seen:
                    # hash 값이 같을때 더블체크.
                    for i in seen[h]:
                        if nums1[i:i+length] == nums2[j:j+length]:
                            return True
            return False
                
        
        while l <= r:
            m = (l+r)//2
            if solve(m):
                ans = m
                l = m+1
            else:
                r = m-1
        return ans
            