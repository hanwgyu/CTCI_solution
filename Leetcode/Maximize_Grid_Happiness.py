# Solution 1: dfs. 0,1(introvert),2(extrovert)로 모두 칠해가면서 모든 경우의 수 체크
# memory 써서 통과!

# Solution 2 : dp. 이전 row의 state와 남은 사람의 수에 따라 happiness를 저장해나아감.

from enum import Enum

class Type(Enum):
    NONE = 0
    INTRO = 1
    EXTRO = 2

def memoization(func):
    memo = dict()
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return wrapper

class Solution:
    def checkHappiness(self, i, a, type):
        if type == Type.NONE:
            return 0
        ans = 0
        if i > 0 and a[i-1] != Type.NONE:
            ans += (-30) if type == Type.INTRO else 20
            ans += (-30) if a[i-1] == Type.INTRO else 20
        if a[i] != Type.NONE:
            ans += (-30) if type == Type.INTRO else 20
            ans += (-30) if a[i] == Type.INTRO else 20
        return ans + 120 if type == Type.INTRO else ans+40
    
    def getMaxGridHappiness_2(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
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
        @memoization
        def dfs(i, j, intro, extro, a):
            a = list(a)
            if i == m:
                if j == n-1:
                    return 0
                return dfs(0, j+1, intro, extro, tuple(a))
            ans = 0
            if intro > 0:
                diff = self.checkHappiness(i, a, Type.INTRO)
                temp, a[i] = a[i], Type.INTRO
                ans = max(ans, dfs(i+1, j, intro-1, extro, tuple(a)) + diff)
                a[i] = temp
            if extro > 0:
                diff = self.checkHappiness(i, a, Type.EXTRO)
                temp, a[i] = a[i], Type.EXTRO
                ans = max(ans, dfs(i+1, j, intro, extro-1, tuple(a)) + diff)
                a[i] = temp
            temp, a[i] = a[i], Type.NONE
            ans = max(ans, dfs(i+1, j, intro, extro, tuple(a)))
            a[i] = temp
            return ans
        if m > n:
            m, n = n, m
        a = [Type.NONE for _ in range(m)]   
        return dfs(0, 0, introvertsCount,extrovertsCount, tuple(a))
