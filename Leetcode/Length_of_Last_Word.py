# Time : O(N), Space: O(1)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ret, reset = 0, False
        for c in s:
            if c == " ":
                reset = True
            else:
                if reset:
                    ret, reset = 0, False
                ret += 1
        return ret
