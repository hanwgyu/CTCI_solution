# 비트를 swap한다는 건, ab -> (a-x)*(b+x) = ab+x(a-b-x) 로 변경한다는 의미.
# 값이 작아지려면 a-b-x < 0. a<b이어야 값이 제일 커짐. 즉, 작은값은 더 작게, 큰값은 더 크게.
# p=4이면 [0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111]
# [0, N-2], [1,N-3],.... 페어로 swap해서 [0001, 1110]을 만듬.
# Time : O(p), Space : O(1)

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = pow(10, 9) + 7
        return (pow(pow(2, p) - 2, pow(2, p-1) - 1, mod) * (pow(2, p) - 1)) % (mod)
