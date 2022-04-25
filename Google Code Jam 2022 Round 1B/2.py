"""
압력을 입력하면 자동으로 바람을 넣어주는 기계. 1 pascal 증가 / 감소 두가지 버튼

N 명의 손님, 손님마다 P개의 제품.
특정 손님의 제품들의 순서를 바꿀 수 있다.

압력 0에서 시작해서 아무 값으로 끝나도 상관없음.

가장 버튼을 적게 누르고 모든 바람을 다 넣는 방법?
"""

"""
무게는 항상 작은쪽에서 큰쪽으로 키우거나 큰쪽에서 작은쪽으로 줄여야함.
모든 두가지 케이스를 고려함.
"""

from collections import defaultdict

def solution():
    def solve():
        N, P = map(int, input().split())
        ltoh, htol = (0,0), (0,0) #(ans, pressure)

        for _ in range(N):
            pressures = sorted(map(int, input().split()))
            ltoh_ = (min(ltoh[0]+abs(ltoh[1]-pressures[0])+(pressures[-1] - pressures[0]), htol[0]+abs(htol[1]-pressures[0])+(pressures[-1] - pressures[0])), pressures[-1])
            htol_ = (min(ltoh[0]+abs(ltoh[1]-pressures[-1])+(pressures[-1] - pressures[0]), htol[0]+abs(htol[1]-pressures[-1])+(pressures[-1] - pressures[0])), pressures[0])
            ltoh, htol = ltoh_, htol_
        return min(ltoh[0], htol[0])

    for T in range(1,1+int(input())):
        ans = solve()
        print("Case #%d:" % T, ans)

solution()
