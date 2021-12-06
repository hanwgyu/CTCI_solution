# 오일러 경로.
# out, in degree 차이가  1인 곳에서 시작. 1인 곳이 없으면 아무곳에서나 시작.

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        ans = []
        d = defaultdict(list)

        degree = defaultdict(int)
        for src, dst in pairs:
            d[src].append(dst)
            degree[src] += 1
            degree[dst] -= 1

        x = pairs[0][0]
        for k in degree:
            if degree[k] == 1:
                x = k
                break

        def dfs(src: int):
            while d[src]:
                dfs(d[src].pop())
            ans.append(src)

        dfs(x)
        ans = ans[::-1]
        return [[ans[i-1], ans[i]] for i in range(1, len(ans))]
