# 완성되지 않은 ]의 최대 갯수를 세고, 절반 이상만큼 swap하면 됨.
# Time : O(N), Space : O(1)

class Solution:
    def minSwaps(self, s: str) -> int:
        a, b = 0, 0
        for c in s:
            if c == '[':
                a += 1
            else:
                a -= 1
            b = min(b, a)
        return (abs(b)+1)//2
