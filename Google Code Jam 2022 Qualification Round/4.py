from collections import defaultdict
from collections import deque
import bisect
import math

from itertools import permutations
from typing import Set

"""
문제 설명 : graph가 있을때, inbound가 0인 노드에서 시작해서 방문.
이미 방문한 노드는 방문할 수 없다.
이런식으로 했을때 모든 루트의 maximum cost의 합이 최대가 되는 방법을 찾아라

1. 모든 케이스를 iterate.
TLE.


"""

def solution():
    def solve():
        N = int(input())
        costs = list(map(int, input().split()))
        targets = list(map(int, input().split()))
        inbounds = [0 for _ in range(N)]
        for target in targets:
            if target != 0:
                inbounds[target-1] += 1
        starts = []
        for i, inbound in enumerate(inbounds):
            if inbound == 0:
                starts.append(i+1)

        def dfs(src, visited: Set[int]):
            if src in visited:
                return 0
            visited.add(src)
            return max(costs[src-1], dfs(targets[src-1], visited))

        ans = 0
        for perm in permutations(starts, len(starts)):
            s, visited = 0, set([0])
            for src in perm:
                s += dfs(src, visited)
            ans = max(ans, s)
        return ans


    for T in range(1,1+int(input())):
        ans = solve()
        print("Case #%d:" % T, ans)

solution()
