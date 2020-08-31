# Solution 1 : 모든 조합에 대해 공약수 가지고 있는지 체크하고, Union-find로 합침.
# Time : O(N^2 * logM) (M은 리스트의 가장 큰 숫자),  Space : O(N)
# Time Limit Exceeded.

# Solution 2 : 각 숫자를 구성하는 소수들에 대한 set을 만든 후, set들을 하나씩 비교하며 합침.
# Time Limit Exceeded. 3792 ms

# Solution 3 : 각 숫자를 구성하는 소수들에 대한 set을 만든 후, 소수들을 Union-find로 합침.
# by 1), 3308ms -> 396ms

import math
from typing import Set


class Solution:
    def findPrimeFactors(self, a: int) -> Set[int]:
        factor, prime_factors = 2, set()
        while a >= (factor * factor):
            if a % factor == 0:
                a //= factor
                prime_factors.add(factor)
            else:
                factor += 1
        prime_factors.add(a)
        return prime_factors

    def largestComponentSize_3(self, A: List[int]) -> int:
        def find(a: int) -> int:
            while a != d[a][0]:
                a = d[a][0]
            return a

        def union(a: int, b: int):
            ra, rb = find(a), find(b)
            if ra != rb:
                # 1) 큰 set에 작은 set을 union하도록 구현. find 비용 줄일 수 있음.
                if d[ra][1] > d[rb][1]:
                    ra, rb = rb, ra
                d[ra][0] = rb
                d[rb][1] += d[ra][1]

        d, values = {}, {}
        for a in A:
            # a의 prime factor들을 union 으로 연결
            s = list(self.findPrimeFactors(a))
            # a를 표현하는 값을 저장
            values[a] = s[0]
            for e in s:
                if not e in d:
                    d[e] = [e, 1]
            for i in range(len(s) - 1):
                union(s[i], s[i + 1])
        sizes = defaultdict(int)
        for a in A:
            sizes[find(values[a])] += 1
        return max(sizes.values())

    def largestComponentSize_2(self, A: List[int]) -> int:
        s = [[self.findPrimeFactors(a), 1] for a in A]
        i = 0
        # 겹치는 부분들을 합침
        while i < len(s):
            j = i + 1
            is_combined = False
            while j < len(s):
                if j != i and s[i][0].intersection(s[j][0]):
                    s[i][0].update(s[j][0])
                    s[i][1] += s[j][1]
                    s.pop(j)
                    is_combined = True
                else:
                    j += 1
            if not is_combined:
                i += 1
        return max(s, key=lambda e: e[1])[1]

    def largestComponentSize_1(self, A: List[int]) -> int:
        def checkCommonFactor(a: int, b: int) -> bool:
            for i in range(2, int(max(math.sqrt(min(a, b)), min(a, b))) + 1):
                if a % i == 0 and b % i == 0:
                    return True
            return False

        def find(a: int) -> int:
            while d[a][0] != a:
                a = d[a][0]
            return a

        def union(a: int, b: int):
            ra, rb = find(a), find(b)
            if ra != rb:
                d[ra][0] = rb
                d[rb][1] += d[ra][1]

        d = {}
        for a in A:
            d[a] = [a, 1]
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a, b = A[i], A[j]
                if checkCommonFactor(a, b):
                    union(a, b)
        return max(d.values(), key=lambda e: e[1])[1]
