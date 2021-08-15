# 인수가 세개려면 소수의 제곱이여야함.

class Solution:
    def isThree(self, n: int) -> bool:
        return int(sqrt(n)) * int(sqrt(n)) == n and int(sqrt(n)) in { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 }
