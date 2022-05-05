"""
Interactive problem

문제 설명: 
8bit의 숫자로 구성된 DB.

새 값 V로 변경시
- 0~7 right rotate를 실행해 W를 만든다
- 이전값 X를 X^W로 교체한다.
- 새 값에서 1인 비트수를 반환한다.

초기값과 rotate 값에 상관없이 300번 미만의 작업을 통해 모든 비트를 0으로 만들 수 있는 DB를 구현하라.


Input
- 00000000 이 아닌 초기값으로 설정된다.
- 우리는 이값을 모른 채로 새로 바꿀 값을 입력해주면 1의 갯수를 리턴 받는다. 300번 미만으로 입력해 00000000으로 만들것.
"""

"""
적대적이여도 통과하려면 01010101을 만들고,
01010101, 11111111를 차례로 넣는다.

"""

from random import randint, shuffle, choice

def solution():
    def solve():
        twos = ["00000011", "000000"]
        V = "11111111"
        for _ in range(300):
            print(V, flush = True)
            N = int(input())
            if N == 0:
                return
            elif N == -1:
                assert False
            elif N == 8:
                V = "11111111"
            else:
                l = ["1" for _ in range(N)]+["0" for _ in range(8-N)]
                shuffle(l)
                V = "".join(l)
        assert False 

    for T in range(1,1+int(input())):
        ans = solve()

solution()
