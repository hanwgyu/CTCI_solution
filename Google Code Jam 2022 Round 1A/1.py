

"""
문제 설명 : 문자가 주어지고, 원하는대로 문자열의 각 문자를 복사할 수 있다. 


그다음 문자와 순서를 비교해서 복사할지 결정. 
그다음 문자와 같으면 복사하지 않고 기다렸다가 진행.
O(N) / O(1)
"""

"""
PEEL => PEEEEL
AAAAAAAAAA => AAAAAAAAAA
CODEJAMDAY => CCODDEEJAAMDAAY
BBA => BBA
AAB => AAAAB
BBAAACC => BBAAAAAACC
"""

def solution():
    def solve():
        ans = []
        s = input()
        repeated = 1
        for i in range(len(s)-1):
            c, cn = s[i], s[i+1]
            ans.append(c)
            if cn > c :
                for _ in range(repeated):
                    ans.append(c)
                repeated = 1
            elif cn == c:
                repeated += 1
            else:
                repeated = 1
        return "".join(ans+[s[-1]])

    for T in range(1,1+int(input())):
        ans = solve()
        print("Case #%d:" % T, ans)

solution()
