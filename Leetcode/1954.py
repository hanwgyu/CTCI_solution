# 고민 1 : centor에서 길이가 n일때, perimeter는 8n
# 사과 개수는 (2n+1) * n * (n+1) * 2
# Time : O(neededApples^(1/3)), Space : O(1)

# 고민 2 : Binary search 로 찾음.
# n이 100000 일때 사과 개수가 4 * 10^15
# Time : O(log(X^(1/3)))(X: neededApples 최대 범위), Space : O(1)

# 4등분 나눠서 계산하면 . 시그마(2a-1) - 시그마(a) + 시그마(2a) - 시그마(a-1) = 3a^2.
# 전체합은 시그마(12a^2) = (2a+1)a(a+1)*2
# [4 3 2 3][4
# [3        3
#  2        2
#  3        3]
#  4][3 2 3 4]
class Solution:
    def minimumPerimeter_2(self, neededApples: int) -> int:
        l, r = 0, 100000
        while l <= r:
            m = (l+r)//2
            apples = (2 * m + 1) * m * (m + 1) * 2
            if apples >= neededApples:
                r = m - 1
            else:
                l = m + 1
        return 8 * l


    def minimumPerimeter_1(self, neededApples: int) -> int:
        n = 1
        while True:
            if (2*n + 1) * n * (n + 1) * 2 >= neededApples:
                break
            n += 1
        return 8 * n
