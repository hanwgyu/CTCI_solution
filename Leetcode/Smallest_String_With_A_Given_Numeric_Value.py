# Solution : 최대한 a와 z로 만들고, 나머지 하나만 다른 알파벳으로 구성.
# Time : O(N), Space : O(1)


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # a를 모두 깔고 뒤부터 z로 바꿈.
        q, r = divmod(k-n, 25)
        return (n - q - (r>0)) * "a" + chr(ord('a') + r) * (r>0) + q * "z"
    
    def getSmallestString(self, n: int, k: int) -> str:
        q, r = divmod(k, 26)
        while n - q >= r:
            q, r = q - 1, r + 26
        return (n - q - 1) * "a" + chr(96 + r - (n - q - 1)) + q * "z"
