class OrderedStream:
    def __init__(self, n: int):
        self.d = {}
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        if id == self.ptr:
            ans = [value]
            while (id + 1) in self.d:
                ans.append(self.d[id + 1])
                id += 1
            self.ptr = id + 1
            return ans
        self.d[id] = value


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
