# Solution : 최대한 a와 z로 만들고, 나머지 하나만 다른 알파벳으로 구성.
# Time : O(1), Space : O(1)


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        q, r = divmod(k, 26)
        while n - q >= r:
            q, r = q - 1, r + 26
        return (n - q - 1) * "a" + chr(96 + r - (n - q - 1)) + q * "z"
