# 문제 설명 : 처음 startFuel의 연료를 가지고 target까지 이동해야함. 1만큼 이동하는데 1만큼의 연료가 필요함. 
# stations은 [station의 위치, 연료량] 의 배열. 연료통의 크기는 무한대라고 가정.
# 최소로 방문하는 station의 갯수를 리턴.

# 직진하면서 연료가 부족해지면 지금까지 지나온 곳들 중에서 가장 연료가 많은 곳을 선택하여 충전.

# O(NlogN) / O(N) # N : len(stations)

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        res = 0
        pq = []
        stations.append([target, 0])
        for pos, fuel in stations:
            while pos > startFuel:
                if not pq:
                    return -1
                startFuel+= -heapq.heappop(pq)
                res += 1
            heapq.heappush(pq, -fuel)
        return res