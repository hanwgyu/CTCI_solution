from collections import defaultdict

# Space : O(N)

class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)
        
    # Time : O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
       
    # Time : O(logN)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        #tuple에 대해 검사하면 첫번쨰 원소 검사이후 두번쨰 원소 검사.
        # 두번째 원소를 ''로 놓아 timestamp보다 큰 원소들중 가장 첫번째 값을 리턴받음.
        idx = bisect.bisect_right(self.d[key], (timestamp+1, ''))
        return '' if idx == 0 else self.d[key][idx-1][1]
    
        
