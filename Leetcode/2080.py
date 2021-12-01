import bisect

class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.d = defaultdict(list)
        for i, a in enumerate(arr):
            self.d[a].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        return bisect.bisect_right(self.d[value], right) - bisect.bisect_left(self.d[value], left)