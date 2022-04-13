"""
문제 설명 : 2N 사이즈의 모두 다른 원소를 가진 어레이가 주어질때, 합이 같은 두 어레이로 나눠라.

1 <= input <= 10^9
"""

from typing import List
import copy

def solution():
    """
        def solve():
        N = int(input())
        A = [i+1 for i in range(N)]
        # phase 1
        print(" ".join(map(str, A)))

        # phase 2
        for c in input().split():
            #A.append(int(c))
            break

        # print answer
        print(A)
    """
    def solve():
        """
        dfs로 모두 계산
        """
        N = int(input())
        A = [i+1 for i in range(N)]
        # phase 1
        print(" ".join(map(str, A)))

        # phase 2
        for c in input().split():
            A.append(int(c))

        # Solve, print answer
        A.sort()
        ans = []
        def dfs(i: int, target: int, array=[]):
            if target == 0:
                ans.extend(copy.deepcopy(array))
                return
            for j in range(i, len(A)):
                if target-A[j] >= 0:
                    array.append(A[j])
                    dfs(j+1, target-A[j], array)
                    array.pop()
                else:
                    break
        dfs(0, sum(A)//2)
        print(" ".join(map(str, ans)))


    for T in range(1,1+int(input())):
        ans = solve()

solution()
