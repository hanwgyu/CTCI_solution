# quality 비율에 맞게 임금을 받아야함. wage보단 많이 받아야함.

# quality / wage 비율을 구하고 하나를 1로 기준뒀을때 1이 넘어가면 wage 지급가능.
# 1보다 큰 것들 중에 quality가 작은 k-1개를 구함.
# 두 값들간의 비율을 통해 1이 넘어가는지 확인가능.
# => 비율이 아니라 그냥 크기로 비교할 수 있다.
# sorting 한 후, 특정 위치에서 오른쪽에 있는 원소들을 선택할 수 있고, quality가 작은 k개를 선택.

"""
10/70 5/30 20/50

특정 원소를 기준으로
sum(quality) / (quality/wage)가 최소인 조합을 구해야함.
"""

# 고민 1: 전체 iteration 돌자.
# Time Limit Exceeded.

# 고민 2: k개의 sum에 대한 계산량을 줄일수 있는법?
# 뒷부분을 quality 기준으로 sorting해서 k-1개 선택.
# Time : O(N^2logN), Space : O(N)

# 고민 3: sum을 windowing 해서 매번 sorting 하지 않음.
# sorting 대신 heap 사용하고, 뒤부터 계산하면서 sliding window식으로 계산!
# 진짜 중요하고 어려운 문제.
# Time : O(NlogN), Space: O(N)

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        N = len(quality)
        a = []
        for i, (q, w) in enumerate(zip(quality, wage)):
            a.append((q/w, q))
        a.sort()

        ans = float('inf')
        h = []
        s = 0
        for i in reversed(range(N)):
            heapq.heappush(h, -a[i][1])
            s += a[i][1]

            if len(h) > k:
                s += heapq.heappop(h)

            if len(h) == k:
                ans = min(ans, s / a[i][0])
        return ans


    def mincostToHireWorkers_2(self, quality: List[int], wage: List[int], k: int) -> float:
        N = len(quality)
        a = []
        for i, (q, w) in enumerate(zip(quality, wage)):
            a.append((q/w, q, i))
        a.sort()
        ans = float('inf')
        for i in range(N-k+1):
            sorted_a = sorted(a[(i+1):], key=lambda s:s[1])
            s = sum(q for _, q, _ in sorted_a[0:k-1])
            ans = min(ans, (quality[a[i][2]] + s) / a[i][0])
        return ans


    def mincostToHireWorkers_1(self, quality: List[int], wage: List[int], k: int) -> float:
        N = len(quality)
        a = []
        for i, (q, w) in enumerate(zip(quality, wage)):
            a.append((q/w, i))
        a.sort()
        ans = float('inf')
        for i in range(N-k+1):
            for c in itertools.combinations(range(i+1, N), k-1):
                ans = min(ans, (quality[a[i][1]] + sum(quality[a[j][1]] for j in c)) / a[i][0])
        return ans
