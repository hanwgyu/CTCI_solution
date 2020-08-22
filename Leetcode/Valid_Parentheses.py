# Time complexity : O(N), Space complexity : O(N)
class Solution(object):
    def isValid_2(self, s: str) -> bool:
        st = []
        d = {"{": "}", "[": "]", "(": ")"}

        for c in s:
            if c in d.keys():
                st.append(c)
            elif c in d.values():
                if not st or d[st.pop()] != c:
                    return False
        return not st

    def isValid_1(self, s):
        # Solution : Use stack

        # Constants
        ROUND, CURLY, SQUARE = 1, 2, 3

        stack = []
        for i in range(len(s)):
            # If left-side
            if s[i] == "(":
                stack.append(ROUND)
            elif s[i] == "{":
                stack.append(CURLY)
            elif s[i] == "[":
                stack.append(SQUARE)
            # If right-side
            elif not stack:
                return False
            elif s[i] == ")" and stack.pop() != ROUND:
                return False
            elif s[i] == "}" and stack.pop() != CURLY:
                return False
            elif s[i] == "]" and stack.pop() != SQUARE:
                return False
        if stack:
            return False
        return True
