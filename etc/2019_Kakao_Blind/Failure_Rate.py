from collections import defaultdict

def solution(N, stages):
    fails, d = [], [0]*(N+1)
    for s in stages:
        if s <= N:
            d[s] += 1
    n = len(stages)
    for i in range(1, N+1):
        if n <= 0:
            fails.append((0, i))
            continue
        fails.append((d[i]/n, i))
        n -= d[i]
    return [e[1] for e in sorted(fails, key= lambda f : -f[0])]
