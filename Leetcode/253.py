# range들을 최대한 합쳤을때 필요한 범위 갯수

# REMIND : 아래와 같이 두가지 방법으로 풀수 있는데, 두번째 방법이 훨씬 낫다. 그 로직 흐름을 잘 이해해서 적용하는게 중요하다.

class Solution:
    def minMeetingRooms(self, intervals):
        """
        골때리는 풀이. [start, 1], [end,-1] 로 만들어서 전체를 sorting한후 진행.
        """
        res = cur = 0
        for i, v in sorted(x for i,j in intervals for x in [[i, 1], [j, -1]]):
            cur += v
            res = max(res, cur)
        return res
    
    
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
            start range를 기준으로 sorting.
            heapq를 써서 진행.
            
            처음 풀었던 방법과 다르게, start 값을 순서대로 소팅하면, 항상 맨 앞 값을 꺼내서 비교해도 그게 최선의 방법이 된다.
        """
        l = []
        for start, end in sorted(intervals):
            if l and l[0] <= start:
                heapq.heapreplace(l, end)
            else:
                heapq.heappush(l, end)
        return len(l)
        
    
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        """
            end range를 기준으로 sorting 후, end range들을 저장해가면서 리스트를 만들어간다.
            start 에 가장 가까운 end 값을 바꾸거나, 없으면 새로 추가한다. 
            그를 위해 binary search 를 사용.
        """
        l = []
        for start, end in sorted(intervals, key=lambda e:e[1]):
            i = bisect.bisect_right(l, start)
            if i != 0:
                l.pop(i-1)
            l.append(end)
        return len(l)
