# Solution 1: dfs. 0,1(introvert),2(extrovert)로 모두 칠해가면서 모든 경우의 수 체크
# Time limit exceeded.

# Solution 2 : dp. 이전 row의 state와 남은 사람의 수에 따라 happiness를 저장해나아감.

from enum import Enum

class Type(Enum):
    NONE = 0
    INTRO = 1
    EXTRO = 2

class Solution:
    def checkHappiness(self, i, a, type):
        ans = 0
        if i > 0 and a[i-1] != Type.NONE:
            ans += (-30) if type == Type.INTRO else 20
            ans += (-30) if a[i-1] == Type.INTRO else 20
        if a[i] != Type.NONE:
            ans += (-30) if type == Type.INTRO else 20
            ans += (-30) if a[i] == Type.INTRO else 20
        return ans + 120 if type == Type.INTRO else ans+40
    
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        def updateHappiness(i, intro, extro, happiness, a, d, type):
            diff = self.checkHappiness(i, a, type)
            temp, a[i] = a[i], type
            if type == Type.INTRO:
                intro -= 1
            elif type == Type.EXTRO:
                extro -= 1
            d[(intro, extro)][tuple(a)] = max(d[(intro, extro)][tuple(a)], happiness+diff)
            a[i] = temp
            self.ans = max(self.ans, happiness+diff)
            
        if m > n:
            m, n = n, m
        pre_d = defaultdict(lambda:defaultdict(int))  # key : intro, extro, key : a
        pre_d[(introvertsCount, extrovertsCount)][tuple([Type.NONE for _ in range(m)])] = 0
        self.ans = 0
        for j in range(n):
            for i in range(m):
                d = defaultdict(lambda:defaultdict(int))
                for intro, extro in pre_d.keys():
                    for a, happiness in pre_d[(intro, extro)].items():
                        a = list(a)
                        # check introvert
                        if intro > 0:
                            updateHappiness(i, intro, extro, happiness, a, d, Type.INTRO)
                        # check extrovert
                        if extro > 0:
                            updateHappiness(i, intro, extro, happiness, a, d, Type.EXTRO)
                        # check none    
                        updateHappiness(i, intro, extro, happiness, a, d, Type.NONE)
                pre_d = d
        return self.ans
   
    def getMaxGridHappiness_1(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        def dfs(i, j, intro, extro, happiness, d):
            if m*n-(j*m+i) < intro + extro:
                return
            if i == m:
                if j == n-1:
                    self.ans = max(self.ans, happiness)
                    return
                dfs(0, j+1, intro, extro, happiness,d)
                return
            if intro > 0:
                diff = self.checkHappiness(i, d, Type.INTRO)
                temp, d[i] = d[i], Type.INTRO
                dfs(i+1, j, intro-1, extro, happiness+diff,d)
                d[i] = temp
            if extro > 0:
                diff = self.checkHappiness(i, d, Type.EXTRO)
                temp, d[i] = d[i], Type.EXTRO
                dfs(i+1, j, intro, extro-1, happiness+diff,d)
                d[i] = temp
            temp, d[i] = d[i], Type.NONE
            dfs(i+1, j, intro, extro, happiness,d)
            d[i] = temp
            
        if m > n:
            m, n = n, m
        d = [Type.NONE for _ in range(m)]   
        self.ans = float('-inf')
        dfs(0,0,introvertsCount,extrovertsCount,0,d)
        return self.ans
