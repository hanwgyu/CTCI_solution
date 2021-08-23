# 두가지 숫자로 이루어진 가장 긴 subarray 찾기

# dp. 한가지 숫자로 이루어진 가장 긴 길이와, 두가지 숫자로 이루어진 가장 긴 길이 저장.
# Time : O(N), Space : O(1)

class Solution:
    def totalFruit(self, A: List[int]) -> int:
        dp1, dp2 = 1, 1
        second = -1 # 현재 값이 아닌 두번째 값을 저장
        ans = 1
        for i, a in enumerate(A[1:], 1):
            if A[i-1] == A[i]:
                dp1, dp2 = dp1+1, dp2+1
            else:
                dp2 = dp2+1 if second == a else dp1+1
                dp1 = 1
                second = A[i-1]
            ans = max(ans, dp2)
        return ans
