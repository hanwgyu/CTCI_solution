# 문제 해설 : 버스를 갈아타면서 source -> target까지 이동하기.
# 최소의 버스 수를 리턴.

# visited + bfs

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_bus = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_bus[stop].append(bus)
    
        visited_stop = set()
        visited_bus = set()
        q = deque([(source, 0)]) # (source, )
        while q:
            stop, n = q.popleft()
            if stop in visited_stop:
                continue
            if stop == target:
                return n
            visited_stop.add(stop)
            for bus in stop_to_bus[stop]:
                if bus not in visited_bus:
                    for s in routes[bus]:
                        if s not in visited_stop:
                            q.append((s, n+1))
                    visited_bus.add(bus)
        return -1