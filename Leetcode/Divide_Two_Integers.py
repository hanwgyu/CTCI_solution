# Solution : 계산량을 줄이기 위해 divisor를 2배씩 증가시켜가며 계산.
# Time : O(log(N)) : Space : O(1)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos = True if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else False
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            temp, i = divisor, 0
            while dividend >= temp:
                ans, dividend, i, temp = ans + (1 << i), dividend - temp, i + 1, temp << 1
        ans = ans if pos else -ans
        return ans if -2**31 <= ans <= 2**31 - 1 else 2**31 - 1 
