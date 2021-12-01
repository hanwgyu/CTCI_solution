# 모든 경우 체크하는데, 좀더 스마트하게 다음 숫자를 만들어 낸다.

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def fn(x):
            """Return next k-symmetric number."""
            n = len(x)//2
            for i in range(n, len(x)):
                if int(x[i])+1 < k:
                    x[i] = x[-(i+1)] = str(int(x[i])+1)
                    for j in range(n,i):
                        x[j] = x[-(j+1)] = '0'
                    return x
            return ["1"] + ["0"]*(len(x)-1) + ["1"]

        x = ["0"]
        ans = 0
        for _ in range(n): 
            while True:
                x = fn(x)
                val = int("".join(x), k)
                if str(val) == str(val)[::-1]: 
                    break
            ans += val
        return ans