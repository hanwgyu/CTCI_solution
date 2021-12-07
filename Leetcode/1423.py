# sol1 : 모든 경우를 sliding window로 계산
# Time : O(K), Space: O(1)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = s = sum(cardPoints[:k])
        for i in range(1, k+1):
            s += cardPoints[-i] - cardPoints[k-i]
            ans = max(ans, s)
        return ans
