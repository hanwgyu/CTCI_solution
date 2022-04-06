from collections import defaultdict
from collections import deque
import bisect
import math

"""
문제 설명 : 1~Si의 값이 나오는 주사위들로 만들 수 있는 가장 긴 연속한 숫자들의 길이.

sorting 해서 앞에서부터 1부터 키워나가면서 갈수있는 최대 길이. 안되면 더 큰수로 이동.

O(NlogN) / O(1)
"""

def solution():
    def solve():
        N = input()
        A = list(map(int, input().split()))
        ans = 1
        A.sort()
        for a in A:
            if ans > a:
                continue
            ans += 1
        return ans-1

    for T in range(1,1+int(input())):
        ans = solve()
        print("Case #%d:" % T, ans)

solution()
