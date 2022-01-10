# 문제 설명 : s의 substring들의 unique한 문자 갯수의 합을 구하라.

# REMIND : 로직만 잘짜면 어렵지 않다. 재미있는 DP 문제!

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        O(N) 혹은 O(NlogN) 으로 줄일 수 있는 방법?
        각 자리의 문자별로 생각해보자. 양 옆으로 동일한 문자가 또 나오기 전까지 확장할 수 있음.
        O(N) / O(1)
        """
        # 각 문자에 대해 지난 두 과거의 위치를 저장해놓으면 됨.
        d = {c:[-1, -1] for c in string.ascii_uppercase}
        res = 0
        for i, c in enumerate(s):
            i0, i1 = d[c]
            # 지난 번 문자에 대해 값을 계산.
            res += (i-i1)*(i1-i0)
            d[c] = [d[c][1], i]
        # 위에서 계산되지 않은 문자에 대해 값을 계산
        for i0, i1 in d.values():
            res += (len(s)-i1)*(i1-i0)
        return res
    
    def uniqueLetterString(self, s: str) -> int:
        """
        DFS로 모든 케이스를 다 돌면서 계산하면 되긴함.
        
        O(N^2) / O(N^2) (S : s 내 문자수)
        Time Limit Exceeded
        """
        visited = set()
        def dfs(i: int, j: int, d: Dict[str, int], u: int) -> int:
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            if i == j:
                return 0
            ans = u
            d[s[i]] -= 1
            ans += dfs(i+1, j, d, u+1 if d[s[i]] == 1 else (u-1 if d[s[i]] == 0 else u))
            d[s[i]] += 1
            d[s[j-1]] -= 1
            ans += dfs(i, j-1, d, u+1 if d[s[j-1]] == 1 else (u-1 if d[s[j-1]] == 0 else u))
            d[s[j-1]] += 1
            return ans
        d = Counter(s)
        u = len(list(c for c in d.values() if c == 1))
        return dfs(0, len(s), d, u)