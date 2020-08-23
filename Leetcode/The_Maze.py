# Solution : 모든 가능한 루트를 방문해봄. 이미 방문한 좌표는 방문하지 않음.

from collections import defaultdict
from typing import Tuple


class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        d = defaultdict(bool)

        def findNextLocations(loc: Tuple[int]) -> List[Tuple[int]]:
            ret = []
            for diff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = loc[0], loc[1]
                while (
                    r >= 0
                    and r < len(maze)
                    and c >= 0
                    and c < len(maze[0])
                    and maze[r][c] == 0
                ):
                    r, c = r + diff[0], c + diff[1]
                if loc[0] != r - diff[0] or loc[1] != c - diff[1]:
                    ret.append((r - diff[0], c - diff[1]))
            return ret

        def dfs(loc: Tuple[int]) -> bool:
            if d[loc]:
                return False
            if loc[0] == destination[0] and loc[1] == destination[1]:
                return True
            d[loc] = True
            for next_loc in findNextLocations(loc):
                if dfs(next_loc):
                    return True
            return False

        return dfs((start[0], start[1]))
