# Solution : use stack
# Time : O(N), Space : O(N)

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, ans = [], [0 for _ in range(len(T))]
        for i, t in enumerate(T):
            while stack and stack[-1][1] < t:
                old_i = stack.pop()[0]
                ans[old_i] = i-old_i
            stack.append((i, t))
        return ans
                
