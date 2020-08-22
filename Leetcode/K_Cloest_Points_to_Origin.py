class Solution(object):
    # Time Complexity : O(NlogK), Space Complexity : O(K)
    def kClosest(self, points, K):
        a = []
        for point in points:
            heapq.heappush(a, (-(point[0] ** 2 + point[1] ** 2), point))
            if len(a) == K + 1:
                heapq.heappop(a)
        return [[i[1][0], i[1][1]] for i in a]

    # Time Complexity : O(NlogN), Space Complexity : O(N)
    def kClosest(self, points, K):
        sorted_points = sorted(
            points, key=lambda point: (point[0] ** 2 + point[1] ** 2)
        )
        return sorted_points[:K]
