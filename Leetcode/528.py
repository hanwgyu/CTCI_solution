class Solution:

    def __init__(self, w: List[int]):
        acc, s = 0, sum(w)
        self.l = []
        for i in w:
            acc += i / s
            self.l.append(acc)

    def pickIndex(self) -> int:
        i = bisect.bisect_right(self.l, random.random())
        return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
