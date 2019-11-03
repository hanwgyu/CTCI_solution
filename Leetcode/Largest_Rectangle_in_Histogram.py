# Solution 0 : heuristics. O(N^2), O(1)

# Solution 1 : 값이 커지면 Stack에 저장, 작아지면 Stack에서 빼서 최대값 계산.
# Stack에서 빼고 새로운 값을 추가할때 i값을 stack에 있던 값들을 고려해 설정.
# Time : O(N), Space : O(N)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s, ans = [], 0
        for i, h in enumerate(heights):
            if not s or s[-1][0] < h:
                s.append((h, i))
            elif s[-1][0] > h:
                new_i = i
                while s and s[-1][0] > h:
                    (old_h, old_i) = s.pop()
                    ans = max(ans, (i - old_i) * old_h)
                    new_i = old_i
                s.append((h, new_i))
        while s:
            (old_h, old_i) = s.pop()
            ans = max(ans, (len(heights) - old_i) * old_h)
        return ans
