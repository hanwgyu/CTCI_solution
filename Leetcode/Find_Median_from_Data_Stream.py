import heapq

#Solution : 두개의 힙을 두고, 갯수는 최대 하나가 차이남. 하나의 힙은 Median보다 작은 값들을 가지고 있고, 최대힙으로 동작.
# 다른 하나의 힙은 Median보다 큰 값들을 가지고 있고, 최소힙으로 동작.

# TimeComplexity : O(logN), O(N)
class MedianFinder(object):
    def __init__(self):
        self.max_heap, self.min_heap = [], [] #max_heap은 minus를 붙인 값을 저장하고있음.
        
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
        
