# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self) -> int:
        n = (rand7() - 1) * 7 + rand7()  # 1 ~ 49
        return self.rand10() if n > 40 else n % 10 + 1
