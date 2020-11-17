# Solution 1 : binary search 한후 add
# Time : O(N^2), Space : O(N).
# Time Limit Exceeded


# Solution 2 : binary index tree. instruction의 갯수를 업데이트해나아감.
# Time : O(MlogM). Space: O(M) # M: max(Instructions)

import bisect


class binaryIndexTree:
    def __init__(self, n: int):
        """ O(1), O(N)  """
        self.a = [0 for _ in range(n + 1)]

    def update(self, i: int, val: int):
        """ O(logN) """
        i += 1
        while i < len(self.a):
            self.a[i] += val
            i += i & -i

    def getSum(self, i: int, j: int) -> int:
        """ O(logN) """

        def getSumFromRoot(i: int) -> int:
            ret = 0
            i += 1
            while i > 0:
                ret += self.a[i]
                i -= i & -i
            return ret

        return getSumFromRoot(j) - getSumFromRoot(i - 1)


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        m = max(instructions)
        bit = binaryIndexTree(m + 1)
        ans = 0
        for i, e in enumerate(instructions):
            ans += min(bit.getSum(0, e - 1), bit.getSum(e + 1, m))
            bit.update(e, 1)
        return ans % (pow(10, 9) + 7)

    def createSortedArray_1(self, instructions: List[int]) -> int:
        a = [instructions[0]]
        d = {instructions[0]: 1}
        ans = 0
        for i in range(1, len(instructions)):
            e = instructions[i]
            j = bisect.bisect_left(a, e)
            if j < len(a) and a[j] == e:
                ans += min(sum(d[e] for e in a[:j]), sum(d[e] for e in a[j + 1 :]))
                d[e] += 1
            else:
                ans += min(sum(d[e] for e in a[:j]), sum(d[e] for e in a[j:]))
                a.insert(j, e)
                d[e] = 1
        return ans % (pow(10, 9) + 7)
