# 생각보다 까다롭고 직관적으로 떠올리기가 어렵다. 좋은 DP문제인듯.
# DP. 각자리에서 해당 숫자로 끝나는 경우의 수를 마지막 값이 0, 1일때로 구분지어서 저장해 나아가면 모든 경우의 수가 겹치는 것 없이 포함됨.
# 현재 숫자가 0일때, dp[0]+dp[1] (0은 제외한다)
# 현재 숫자가 1일때, dp[0]+dp[1]+1 (1만 있는 경우 포함시켜줌)

class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        dp = [0, 0] # 0으로 끝나는 경우의 수, 1로 끝나는 경우의 수
        for b in binary:
            dp[int(b)] = (sum(dp) + int(b)) % (10**9 + 7)
        return (sum(dp) + ('0' in binary)) % (10**9 + 7)
