# Solution 1.
"""
n개의 알파벳이 있을때, n-1 구간동안 최대 4번 증가가능.
a1+a2+...+an-1 <= 4 (ai >= 0)

1) a1+a2+...+an-1 <= n+3 (ai > 0)
4일때 1 * n+2Cn-2
3일때 2 * n+1Cn-2
2일떄 3 * nCn-2
1일때 4 * n-1Cn-2
0일때 5 * n-2Cn-2
=> 1 * n+2Cn-2 + 2 * n+1Cn-2 + 3 * nCn-2 + 4 * n-1Cn-2 + 5 * n-2Cn-2

2) a0+  a1+a2+...+an-1 + an= 4 (ai >= 0)
a0+  a1+a2+...+an-1 + an= n+5 (ai > 0)
=> n+4Cn

"""

# Solution 2 : DP

from math import comb

class Solution:
    def countVowelStrings_2(self, n: int) -> int:
        """O(N) / O(1)"""
        cnt = [1] * 5
        for _ in range(1, n):
            for i in range(5):
                cnt[i] = sum(cnt[i:])
        return sum(cnt)
    
    def countVowelStrings_1(self, n: int) -> int:
        """O(1) / O(1)"""
        return comb(n + 4, n)
        # return 1 * comb(n+2, n-2) + 2 * comb(n+1, n-2) + 3 * comb(n, n-2) + 4 * comb(n-1,n-2) + 5 if n > 1 else 5
