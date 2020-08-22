# Solution : AND(&)로 각 bit자리의 carry를 계산하고, XOR(^)로 각 bit자리의 덧셈 결과를 결정.
# 그 이후, Carry를 다시 더하도록 반복 계산.
# Time : O(1), Space : O(1)


class Solution:
    # 32bit operation
    MASK = 0xFFFFFFFF
    MAX = 0x7FFFFFFF

    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            temp = (a ^ b) & self.MASK
            b = ((a & b) << 1) & self.MASK
            a = temp
        return a if a <= self.MAX else ~(a ^ self.MASK)
