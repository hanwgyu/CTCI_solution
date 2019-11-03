# Solution : stack에 원소를 저장하면서 마이너스값을 가진 운석은 스택내의 플러스값 운석과 싸워서 저장여부를 결정.
# Time : O(N), Space : O(N)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for e in asteroids:
            if e < 0:
                while stack and stack[-1] > 0 and stack[-1] < abs(e):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(e)
                elif stack[-1] == abs(e):
                    stack.pop()
            else:
                stack.append(e)
        return stack
