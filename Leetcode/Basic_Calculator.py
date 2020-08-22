# Time Complexity : O(N), Space Complexity : O(N)
class Solution(object):
    ADD, SUBTRACT = 1, 2

    def operate(self, operand_front, operand_back, operator):
        return (
            (operand_front + operand_back)
            if operator == Solution.ADD
            else (operand_front - operand_back)
        )

    def calculate(self, s):
        # Solution : 괄호 시작시 계산중인 값을 stack에 저장.
        result_stack, operator_stack = [], []
        result, operator, operand = 0, Solution.ADD, 0
        for char in s:
            if char.isdigit():
                operand = operand * 10 + int(char)
            elif char == "+":
                result = self.operate(result, operand, operator)
                operator, operand = Solution.ADD, 0
            elif char == "-":
                result = self.operate(result, operand, operator)
                operator, operand = Solution.SUBTRACT, 0
            elif char == "(":
                result_stack.append(result)
                operator_stack.append(operator)
                result, operator = 0, Solution.ADD
            elif char == ")":
                # calculate inside parentheses
                result = self.operate(result, operand, operator)
                # calculate outside parentheses
                operator = operator_stack.pop()
                old_result = result_stack.pop()
                result = self.operate(old_result, result, operator)
                operand = 0

        return self.operate(result, operand, operator)
