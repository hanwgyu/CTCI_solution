# DP. 각 idx의 원소가 포함된 solution의 최대 원소 갯수를 저장.
# Time : O(NlogN), Space : O(N)

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        predecessor 인거 어떻게 확인? : 그냥 함수 만들면 되긴함. 앞에서부터 비교진행. O(L)
        
        길이 순서대로 sorting 해서 DP로 비교? O(N^2)
        """
        def predecessor(w1: str, w2: str) -> bool:
            if len(w1) != len(w2) + 1:
                return False
            i, j, max_diff = 0, 0, 1
            while i < len(w1) and j < len(w2):
                if w1[i] != w2[j]:
                    if max_diff > 0:
                        max_diff -= 1
                        i += 1
                        continue
                    else:
                        return False
                i, j = i+1, j+1
            return True
        dp = [1 for _ in range(len(words))]
        words.sort(key=len)
        print(words)
        for i, word in enumerate(words):
            for j in range(i):
                if predecessor(word, words[j]):
                    dp[i] = max(dp[i], dp[j]+1)
                    if dp[i] == len(word):
                        break
        return max(dp)

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
