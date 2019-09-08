#brute-force
#(2018년) KAKAO BLIND RECRUITMENT

def solution(relation):
    numCol, n = len(relation[0]), len(relation) 
    comb, keys = [], []
    getComb(numCol-1, comb)
    for c in comb:
        s = set()
        for r in relation:
            com_str = ""
            for i in c:
                com_str += r[i]
            s.add(com_str)
        if len(s) == n:
            key = 0
            for i in c:
                key += 1 << i 
            keys.append(key)
    print(keys)
    ans = 0
    for key in keys:
        if all(key == k or key&k != k for k in keys):
            ans += 1          
    return ans

def getComb(i: int, a):
    if i < 0:
        return
    getComb(i-1, a)
    for j in range(len(a)):
        a.append(a[j]+[i])
    a.append([i])
