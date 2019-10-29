# DP. 각 idx의 원소가 포함된 solution의 최대 원소 갯수를 저장.
# Time : O(NlogN), Space : O(N)

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def checkPredecessor(predecessor: str, target: str) -> bool:
            if len(predecessor) + 1 != len(target):
                return False
            max_diff = 1
            j = 0
            for i in range(len(target)):
                if j >= len(predecessor) or target[i] != predecessor[j]:
                    if max_diff > 0:
                        max_diff -= 1
                    else:
                        return False
                else:
                    j += 1
            return True
        
        words.sort(key=len)
        N = len(words)
        dp = [0] * N
        for i, word in enumerate(words):
            for j in range(i):
                if dp[j] + 1 > dp[i] and checkPredecessor(words[j], word):
                    dp[i] = dp[j] + 1
            dp[i] = max(1, dp[i])
        return max(dp)
