# Solution 1: dfs. 0,1(introvert),2(extrovert)로 모두 칠해가면서 모든 경우의 수 체크
# Time limit exceeded.

# Solution 2 : dp. 이전 row의 state와 남은 사람의 수에 따라 happiness를 저장해나아감.


class Solution:
    def checkHappiness(self, i, d, type):
        ans = 0
        if i > 0 and d[i - 1] != 0:
            ans += (-30) if type == 1 else 20
            ans += (-30) if d[i - 1] == 1 else 20
        if d[i] != 0:
            ans += (-30) if type == 1 else 20
            ans += (-30) if d[i] == 1 else 20
        return ans + 120 if type == 1 else ans + 40

    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        if m > n:
            m, n = n, m
        pre_d = defaultdict(lambda: defaultdict(int))  # key : intro, extro, key : a
        pre_d[(introvertsCount, extrovertsCount)][tuple([0 for _ in range(m)])] = 0
        ans = 0
        for j in range(n):
            for i in range(m):
                d = defaultdict(lambda: defaultdict(int))
                for intro, extro in pre_d.keys():
                    for a, happiness in pre_d[(intro, extro)].items():
                        a = list(a)
                        # check introvert
                        if intro > 0:
                            diff = self.checkHappiness(i, a, 1)
                            temp, a[i] = a[i], 1
                            d[(intro - 1, extro)][tuple(a)] = max(d[(intro - 1, extro)][tuple(a)], happiness + diff)
                            a[i] = temp
                            ans = max(ans, happiness + diff)
                        # check extrovert
                        if extro > 0:
                            diff = self.checkHappiness(i, a, 2)
                            temp, a[i] = a[i], 2
                            d[(intro, extro - 1)][tuple(a)] = max(d[(intro, extro - 1)][tuple(a)], happiness + diff)
                            a[i] = temp
                            ans = max(ans, happiness + diff)
                        temp, a[i] = a[i], 0
                        d[(intro, extro)][tuple(a)] = max(d[(intro, extro)][tuple(a)], happiness)
                        a[i] = temp
                        ans = max(ans, happiness)
                pre_d = d
        return ans

    def getMaxGridHappiness_1(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        def dfs(i, j, intro, extro, happiness, d):
            if m * n - (j * m + i) < intro + extro:
                return
            if i == m:
                if j == n - 1:
                    self.ans = max(self.ans, happiness)
                    return
                dfs(0, j + 1, intro, extro, happiness, d)
                return
            if intro > 0:
                diff = self.checkHappiness(i, d, 1)
                temp, d[i] = d[i], 1
                dfs(i + 1, j, intro - 1, extro, happiness + diff, d)
                d[i] = temp
            if extro > 0:
                diff = self.checkHappiness(i, d, 2)
                temp, d[i] = d[i], 2
                dfs(i + 1, j, intro, extro - 1, happiness + diff, d)
                d[i] = temp
            temp, d[i] = d[i], 0
            dfs(i + 1, j, intro, extro, happiness, d)
            d[i] = temp

        if m > n:
            m, n = n, m
        d = [0 for _ in range(m)]
        self.ans = float("-inf")
        dfs(0, 0, introvertsCount, extrovertsCount, 0, d)
        return self.ans
