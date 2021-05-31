import heapq



class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        #self.min_h 가 self.max_h 보다 한개 많거나 갯수가 같도록 유지시킴
        self.min_h, self.max_h = [], []

    def addNum(self, num: int) -> None:
        if self.min_h and -self.min_h[0] < num:
            heapq.heappush(self.max_h, num)
        else:
            heapq.heappush(self.min_h, -num)
        while len(self.min_h) - len(self.max_h) > 1:
            n = -heapq.heappop(self.min_h)
            heapq.heappush(self.max_h, n)
        while len(self.max_h) - len(self.min_h) > 0:
            n = heapq.heappop(self.max_h)
            heapq.heappush(self.min_h, -n)

    def findMedian(self) -> float:
        if (len(self.min_h) + len(self.max_h)) % 2 == 0:
            return (-self.min_h[0] + self.max_h[0]) / 2
        else:
            return -self.min_h[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# Solution : 두개의 힙을 두고, 갯수는 최대 하나가 차이남. 하나의 힙은 Median보다 작은 값들을 가지고 있고, 최대힙으로 동작.
# 다른 하나의 힙은 Median보다 큰 값들을 가지고 있고, 최소힙으로 동작.

# TimeComplexity : O(logN), O(N)
class MedianFinder(object):
    def __init__(self):
        self.max_heap, self.min_heap = [], []  # max_heap은 minus를 붙인 값을 저장하고있음.

    def addNum(self, num):
        len_max, len_min = len(self.max_heap), len(self.min_heap)
        if len_max < len_min:
            if self.min_heap[0] < num:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        elif len_max == 0 and len_min == 0:
            heapq.heappush(self.min_heap, num)
        elif len_max == len_min:
            if self.min_heap[0] < num:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        else:
            if num < -self.max_heap[0]:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)

    def findMedian(self):
        if not self.max_heap and not self.min_heap:
            return None
        len_max, len_min = len(self.max_heap), len(self.min_heap)
        if len_max < len_min:
            return self.min_heap[0]
        elif len_max == len_min:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0]
