# Solution 1 : Heap.
# Time : O(HlogH), Space: O(H)

# Solution 2 : DP. 각 위치에서 사용 ladder수에 따른 최소 사용 bricks수를 저장해나아감.
# Time : O(ladders*H) , Space : O(ladders*H)

import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diffs = []
        h_b = float("inf")
        for i, h in enumerate(heights):
            if h - h_b > 0:
                diffs.append((h - h_b, i))
            h_b = h
        q = []
        i = 0
        while i < len(diffs):
            diff = diffs[i][0]
            if bricks < diff:
                if ladders == 0:
                    return diffs[i][1] - 1
                ladders -= 1
                if q and q[0][1] > diff:
                    bricks += heapq.heappop(q)[1]
                else:  # q의 최대값보다 현재 diff가 더 크면 q에서 꺼내지 않고 현재 값을 ladder로 사용.
                    i += 1
            else:
                heapq.heappush(q, (-diff, diff))
                bricks -= diff
                i += 1
        return len(heights) - 1
