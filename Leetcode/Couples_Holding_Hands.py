# Solution : Union-find. 연속한 두 원소(2i, 2i+1)가 다를때, 각 원소가 속한 idx를 저장해놓음.
# 각 원소들의 idx를 통해 union-find 진행.
# Union 이후 남은 set의 갯수를 전체 원소 갯수에서 빼주면, 필요한 swap횟수가 나오게됨.
# Time : O(N), Space: O(N)
# Set의 swap 갯수 구하기 위한 개념 : Permutation Group. N-permutation group은 N-1개의 2-permutation group의 합성함수로 표현 가능함.


from collections import defaultdict


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def find(i: int) -> int:
            if d[i] != i:
                return find(d[i])
            return i

        N = len(row) // 2
        lo, d = defaultdict(list), {i: i for i in range(N)}
        for i in range(N):
            a, b = row[2 * i] // 2, row[2 * i + 1] // 2
            if a == b:
                continue
            lo[a].append(i)
            lo[b].append(i)
        num_set = N
        for val in lo.keys():
            (lo1, lo2) = lo[val]
            if find(lo1) != find(lo2):
                d[find(lo1)] = find(lo2)
                num_set -= 1
        return N - num_set
