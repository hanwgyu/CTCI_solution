"""
문제 설명 : 2N 사이즈의 모두 다른 원소를 가진 어레이가 주어질때, 합이 같은 두 어레이로 나눠라.

1 <= input <= 10^9
"""

from typing import List
import copy

def solution():
    def solve():
        """
        값의 최대 범위가 10**9 이므로, 29 비트로 표현 가능하다.
        A1에 각 비트에 대한 값들을 저장, A2는 임의의 값을 저장.
        A1, A2를 합쳐 입력으로 넣어주면, B가 나오게됨.
        A+B의 합 s의 절반까지 A2, B로 만들어나가고, 더이상 못합칠때까지 합침.
        그렇게 되면 항상 남는 값은 2*30 미만이고, 해당 값은 A1내의 값으로 항상 만들 수 있다.
        굉장히 똑똑한 풀이!

        O(N) / O(1)
        """

        N = int(input())
        A1 = [2**i for i in range(30)]
        A2 = [10**9-i for i in range(N-30)]
        A = A1+A2

        print(" ".join(map(str, A)))

        *B, = map(int, input().split())

        s = sum(A) + sum(B)

        x = []
        for i in B+A2:
            if 2*(sum(x) + i) <= s:
                x.append(i)

        for i in A1[::-1]:
            if 2*(sum(x)+i) <= s:
                x.append(i)

        assert sum(x)*2 == s, f"{sum(x)*2}, {s}"

        print(" ".join(map(str, x)))

    for T in range(1,1+int(input())):
        ans = solve()

solution()
