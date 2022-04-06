from collections import defaultdict
from collections import deque
import bisect
import math

"""
문제 설명 : interactive 그래프 문제.
그래프 노드를 최대 K번 이동해서 그래프의 전체 vertex 수를 구하라.
이동하면 이동한 노드의 번호와 연결된 간선 수를 알려줌. 

가능한 행동:
1) 현재 노드에 연결된 다른 노드로 랜덤하게 이동
2) 특정 노드로 텔레포트

N : 그래프 노드 갯수, K : 요청 가능한 행동 수

"""

def solution():
    def solve():
        N, K = list(map(int, input().split()))
        for _ in range(K):
            room, passage = list(map(int, input().split()))
            print("W")
        print("E 5")

    for T in range(1,1+int(input())):
        ans = solve()

solution()
