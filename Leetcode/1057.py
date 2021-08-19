# 전체에서 보고 Manhattan distance가 작은 순서 -> worker index가 작은 순서 ->  bike index가 작은 순서대로 배정.

# Sorting
# Time : O(N^2logN), Space : O(N^2)

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def md(worker: List[int], bike: List[int]) -> int:
            return (abs(worker[0]-bike[0]) + abs(worker[1]-bike[1]))
        mds = [] #(md, worker, bike) 순서대로 만들어서 sorting.
        for m, bike in enumerate(bikes):
            for n, worker in enumerate(workers):
                mds.append((md(worker, bike), n, m))
        mds.sort()

        ans = [0] * len(workers)
        used_worker = set()
        used_bike = set()
        for md, n, m in mds:
            if n in used_worker or m in used_bike:
                continue
            ans[n] = m
            used_worker.add(n)
            used_bike.add(m)
        return ans
