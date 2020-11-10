# Time : O(N), Space: O(1)


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        c, directions, d = [0, 0], [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
        # 최대 circle 횟수 : 4회
        for i in range(4):
            for e in instructions:
                if e == "L":
                    d += 1
                elif e == "R":
                    d -= 1
                else:
                    for i in range(len(c)):
                        c[i] += directions[d % len(directions)][i]
            if c == [0, 0]:
                return True
        return False
