# Solution 1 : Use Hash


class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n > 1:
            temp = 0
            while n > 0:
                temp, n = temp + (n % 10) ** 2, n // 10
            n = temp
            if temp not in nums:
                nums.add(temp)
            else:
                return False
        return True
