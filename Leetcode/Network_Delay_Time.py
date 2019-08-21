# Solution : Dijkstra algorithm. 모든 Min distance의 max값을 구함. 
# Time : O(ElogV), Sapce: O(V+E)

from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        visited, min_dis, min_heap = defaultdict(bool), [float('inf') for _ in range(N)], []
        dis = defaultdict(lambda : defaultdict(int))
        for time in times:
            dis[time[0]][time[1]] = time[2]
        min_dis[K-1] = 0
        visited[K] = True
        for dst, time in dis[K].items():
            min_dis[dst-1] = min(min_dis[dst-1], min_dis[K-1]+time)
            heapq.heappush(min_heap, (min_dis[dst-1], K, dst))
        while min_heap and len(visited) != N:
            (time, src, dst) = heapq.heappop(min_heap)
            if dst in visited:
                continue
            visited[dst] = True
            min_dis[dst-1] = min(min_dis[dst-1], min_dis[src-1]+time)
            for new_dst, new_time in dis[dst].items():
                min_dis[new_dst-1] = min(min_dis[new_dst-1], min_dis[dst-1]+new_time)
                heapq.heappush(min_heap, (min_dis[new_dst-1], dst, new_dst))
        return max(min_dis) if len(visited) == N else -1
