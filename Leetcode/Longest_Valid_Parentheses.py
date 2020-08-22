# https://leetcode.com/problems/longest-valid-parentheses/
# Time Complexity : O(N), Space Complexity : O(N)
class Solution(object):
    def longestValidParentheses(self, s):
        # Solution 1 : DP
        total_length = len(s)

        sol = 0
        dp = [
            0
        ] * total_length  # dp[length]는 length위치에 있는 문자를 끝으로 하는 valid한 parentheses의 최대 길이

        for length in range(1, total_length):
            if s[length] == ")":
                if s[length - 1] == "(":
                    dp[length] = (dp[length - 2] if length >= 2 else 0) + 2
                elif (
                    length - dp[length - 1] > 0
                    and s[length - 1 - dp[length - 1]] == "("
                ):
                    dp[length] = (
                        dp[length - 1]
                        + 2
                        + (
                            dp[length - 2 - dp[length - 1]]
                            if length >= 2
                            else 0
                        )
                    )
                if sol < dp[length]:
                    sol = dp[length]
        return sol

    def longestValidParentheses_2(self, s):
        # Solution 2
        # 단어가 ")"이고, 완전히 비지 않았을때 length를 업데이트.
        # 완전히 비었다는 뜻은 비정상적인 문장이 되었다는 뜻으로 더이상 길이를 늘릴수 없다는뜻.
        # 완전히 비었을때는 ")" 위치에 해당하는 idx를 push해줌.
        # 스택의 가장 마지막 원소를 start idx로 씀.

        stack = [-1]

        length, max_length = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack == []:  # stack is empty
                    stack.append(i)
                else:
                    start = stack[-1]
                    length = i - start
                    if max_length < length:
                        max_length = length

        return max_length

    # Time Complexity : O(N), Space Complexity : O(1)
    def longestValidParentheses_3(self, s):
        left, right, max_length = 0, 0, 0

        # Left-to-Right
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left < right:
                left, right = 0, 0
            elif left == right:
                length = 2 * right
                if max_length < length:
                    max_length = length

        left, right = 0, 0
        # Right-to-Left
        for i in reversed(range(len(s))):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left > right:
                left, right = 0, 0
            elif left == right:
                length = 2 * right
                if max_length < length:
                    max_length = length

        return max_length
