from collections import defaultdict
from collections import deque
import bisect
import math

"""
각 색깔의 minimum의 합이 10^6 미만이면 만들수 없음.
그 이상이면 합에서 아무 숫자나 줄여서 리턴.
"""

def solution():
    def solve():
        colors = [float('inf')]*4
        for _ in range(3):
            pcolors = input().split()
            for i in range(4):
                colors[i] = min(colors[i], int(pcolors[i]))
        if sum(colors) < 10**6:
            return "IMPOSSIBLE"
        diff = sum(colors) - 10**6
        i = 0
        while diff > 0:
            if diff > colors[i]:
                diff, colors[i] = diff-colors[i], 0
            else:
                diff, colors[i] = 0, colors[i]-diff
            i += 1
        colors = map(str, colors)
        return " ".join(colors)

    for T in range(1,1+int(input())):
        ans = solve()
        print("Case #%d:" % T, ans)

solution()
