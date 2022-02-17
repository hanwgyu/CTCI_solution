class HitCounter:
    """
    이벤트를 저장하는게 아니라, 단위가 초이므로 300개의 bucket만 만들면 된다.
    오래된 bucket을 지우기 위해 window index를 추가로 저장.

    O(1) / O(1)
    """

    def __init__(self):
        self.count = [[0,0] for _ in range(300)] # (window index, count)

    def hit(self, timestamp: int) -> None:
        wi, i = divmod(timestamp, 300)
        if self.count[i][0] != wi:
            self.count[i] = [wi,0]
        self.count[i][1] += 1

    def getHits(self, timestamp: int) -> int:
        wi, i = divmod(timestamp, 300)
        for j in range(300):
            if j <= i and self.count[j][0] != wi:
                self.count[j] = [wi,0]
            elif j > i and self.count[j][0] != wi-1:
                self.count[j] = [wi,0]
        return sum(self.count[i][1] for i in range(300))


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)