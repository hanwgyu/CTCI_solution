# Solution 1 : 계산량을 줄이기 위해 divisor를 2배씩 증가시켜가며 계산.
# Time : O(log(divisor)) : Space : O(1)

# Solution 2 : 2진수 나누기
# Time : O(1) : Space : O(1)

class Solution:
    def divide_2(self, dividend: int, divisor: int) -> int:
        """O(1) / O(1)"""
        quot, tmp, pos = 0, 0, (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        for i in reversed(range(32)):
            if tmp + (divisor << i) <= dividend:
                tmp += divisor << i
                quot |= 1 << i
        if (1 << 31) - pos < quot: return (1 << 31) - 1
        return [-quot, quot][pos]
    
    def divide_1(self, dividend: int, divisor: int) -> int:
        pos = True if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else False
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            temp, i = divisor, 0
            while dividend >= temp:
                ans, dividend, i, temp = ans + (1 << i), dividend - temp, i + 1, temp << 1
        ans = ans if pos else -ans
        return ans if -2**31 <= ans <= 2**31 - 1 else 2**31 - 1 
