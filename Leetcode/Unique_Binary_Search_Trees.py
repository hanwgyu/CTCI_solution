# Solution : DP. n개의 원소로 만들수 있는 트리 갯수를 구함. 
# n개의 원소로 어떻게든 Binary 트리 형태를 만들면, inorder로 돌면서 BST로 구성할수있고 모두 unique함.
# Root를 어떤 숫자로 둘지가 중요함. Root숫자에 따라 왼쪽과 오른쪽 subtree의 원소 갯수가 결정되어 DP를 통해 계산 가능.
# Time : O(N^2), Space : O(N)

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-1-j]
        return dp[n]
        
        
