# Solution : Stack을 이용해 숫자를 앞에서부터 넣어가면서, Stack마지막 값보다 현재 숫자가 작으면 Stack pop을 하고 현재값을 추가.
# Time : O(N), Space : O(N)

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
