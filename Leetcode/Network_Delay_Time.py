# Solution : Dijkstra algorithm. 모든 Min distance의 max값을 구함.
# Time : O(ElogE), Sapce: O(V+E)

from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Dijikstra : 특정 노드로부터 모든 노드까지의 최소 거리를 저장하고, 거리가 가까운 곳부터 방문하면서 주변 노드까지의 거리를 업데이트.
        
        O((V+E)logE) = O((V+E)logV) , Space: O(V+E)
        """
        cost = defaultdict(lambda: float('inf'))
        adj_list = defaultdict(list)
        h = [(0,k)]# time, src
        visited = set()
        # make adjacent list
        for src, dst, time in times:
            adj_list[src].append((dst, time))
        # start from node k
        cost[k] = 0
        while h and len(visited) < n:
            src_time, src = heapq.heappop(h)
            if src in visited:
                continue
            visited.add(src)
            for dst, time in adj_list[src]:
                if cost[dst] > src_time+time:
                    cost[dst] = src_time+time
                    heapq.heappush(h, (src_time+time, dst))
        return max(cost.values()) if len(visited) == n else -1
                 
    
    
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        visited, min_dis, min_heap = (
            defaultdict(bool),
            [float("inf") for _ in range(N)],
            [],
        )
        dis = defaultdict(lambda: defaultdict(int))
        for time in times:
            dis[time[0]][time[1]] = time[2]
        min_dis[K - 1] = 0
        visited[K] = True
        for dst, time in dis[K].items():
            min_dis[dst - 1] = min(min_dis[dst - 1], min_dis[K - 1] + time)
            heapq.heappush(min_heap, (min_dis[dst - 1], K, dst))
        while min_heap and len(visited) != N:
            (time, src, dst) = heapq.heappop(min_heap)
            if dst in visited:
                continue
            visited[dst] = True
            min_dis[dst - 1] = min(min_dis[dst - 1], min_dis[src - 1] + time)
            for new_dst, new_time in dis[dst].items():
                min_dis[new_dst - 1] = min(
                    min_dis[new_dst - 1], min_dis[dst - 1] + new_time
                )
                heapq.heappush(min_heap, (min_dis[new_dst - 1], dst, new_dst))
        return max(min_dis) if len(visited) == N else -1
