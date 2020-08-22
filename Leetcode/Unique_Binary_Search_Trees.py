# Solution 1 : DP. n개의 원소로 만들수 있는 트리 갯수를 구함.
# n개의 원소로 어떻게든 Binary 트리 형태를 만들면, inorder로 돌면서 BST로 구성할수있고 모두 unique함.
# Root를 어떤 숫자로 둘지가 중요함. Root숫자에 따라 왼쪽과 오른쪽 subtree의 원소 갯수가 결정되어 DP를 통해 계산 가능.
# Time : O(N^2), Space : O(N)

# Solution 2 : Catalan Number.
# T(n) = T(0) * T(n-1) + T(1) * T(n-2) + .... + T(n-1) * T(0)
# 점화식이 카탈란수인데, 직관적으로 길찾기 문제와 어떻게 연결해 이해해야할지 모르겠음.
# T(n) = 2nCn - 2nCn+1 = (1/n+1) * 2nCn
# Time : O(N), Space : O(1)


class Solution:
    def numTrees_2(self, n: int) -> int:
        return (int)(
            math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1))
        )

    def numTrees_1(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]
