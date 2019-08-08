class Solution(object):
    def removeKdigits(self, num, k):
        stack, ans = [], 0
        for i in range(len(num)):
            while k > 0 and stack and stack[-1] > int(num[i]):
                stack.pop()
                k -= 1
            stack.append(int(num[i]))
        while k > 0:
            stack.pop()
            k -= 1
                
        if stack:
            ans = stack[0]
        for i in range(1, len(stack)):
            ans = ans * 10 + stack[i]
        return str(ans)
