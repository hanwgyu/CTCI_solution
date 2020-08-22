# Time : O(N), Space: O(1)


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def getNumOfSigOnes(num: int) -> int:
            cnt = 0
            for i in range(8):
                bit, num = num % 2, num >> 1
                if bit == 1:
                    cnt += 1
                else:
                    cnt = 0
            return cnt

        length = 0
        for num in data:
            n = getNumOfSigOnes(num)
            if length == 0 and n == 0:
                continue
            elif length == 0 and n == 1:
                return False
            elif length == 0 and n < 5:
                length = n - 1
                continue
            elif length == 0:
                return False

            if length != 0 and n == 1:
                length -= 1
                continue
            elif length != 0:
                return False

        return True if length == 0 else False
