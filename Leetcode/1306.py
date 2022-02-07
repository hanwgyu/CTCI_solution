# 문제 설명 : start index에서 시작해서 i - arr[i] 나 i + arr[i] 로 이동. 값이 0인 인덱스로 이동할 수 있는지 확인

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def dfs(i: int) -> bool:
            if i < 0 or i > len(arr)-1 or i in visited:
                return False
            if arr[i] == 0:
                return True
            visited.add(i)
            return any([dfs(i-arr[i]), dfs(i+arr[i])])
        return dfs(start)