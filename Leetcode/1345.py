# BFS + visited
# minimum 길이를 구하니까 BFS+ visited로 하면 됨.

# 계산량을 줄이기 위해 value에 따른 visited를 추가해 관리

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        values = defaultdict(list)
        N = len(arr)
        q = deque([(0, 0)]) # (index, length)
        visited, visited_value = set([0]), set()
        
        for i, e in enumerate(arr):
            values[e].append(i)
        
        while q:
            i, l = q.popleft()
            if i == N-1: return l
            for diff in [-1, 1]:
                x = i + diff
                if 0 <= x < N and x not in visited:
                    q.append((x, l+1))
                    visited.add(x)
            if arr[i] not in visited_value:
                for x in values[arr[i]]:
                    if x not in visited:
                        q.append((x, l+1))
                        visited.add(x)
                visited_value.add(arr[i])
        return 0