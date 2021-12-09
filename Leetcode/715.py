# REMIND: 좋은 Binary search 문제. 다시 확인할것.

# Sol1: start, end 를 따로따로 관리함. increasing order로.
# addRange : left, right를 모두 start에서 binarysearch 해서 같은 index가 나오면 end만 업데이트하고, 다른 index가 나오면 start, end를 병합한다.
# deleteRange : left는 start, right는 end에서 각각 binarysearch시 동일한 index -> 하나의 값을 두개로 나눔. 그게 아니면 아예 없애거나 위치에 따라 변경.
# queryRange : left는 start, right는 end에서 각각 binarysearch시 동일한 index가 되면 return True
# 복잡함.


class RangeModule:
    """    
        Sol2: 하나로 관리하는게 더 낫다

        이런식으로 동작함. 몰랐네.
        >>> a = [1,2,3,4]
        >>> a[1:2] = []
        >>> a
        [1, 3, 4]

        a = [0,1,3,4]
        start는 mod2 가 0이면 추가, end는 mod2가 0이면 추가.
        addRange(1,3) -> [0,4]
        a[1:3] = []
        addRange(2,3) -> [0,1,2,4]
        a[2:3] = [2]
        removeRange(3,4) -> [0,1]
        a[2:4] = []
    """

    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)
        self.track[start:end] = subtrack

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)
        if start == end and start % 2 == 1:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)
        self.track[start:end] = subtrack


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
