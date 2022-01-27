"""
Prime Time

문제 설명 :
카드를 두 그룹으로 나눈다.
첫번째 그룹은 카드의 합을, 두번째 그룹은 곱을 구한다.
두 값이 동일해야할때, 최대인 값은? 불가능하면 0을 리턴하라.

모든 경우를 traverse?
곱하는 비용을 줄일 수 있나? 
1) windowing으로 줄임.  1번은 통과 2번부턴 초과.
2) sum-sum(cards) < 10^19, mul < 10^19. 2만있어도 숫자 수가 최대 68개

3:16 start - 4:16 end

"""

from typing import List
import math

def solution1():
    """
        Time Exceeded
    """
    for T in range(1,1+int(input())):
        N = int(input())
        A, B = [], []
        for _ in range(N):
            p, n= map(int, input().split())
            A.append(p)
            B.append(n)
        print(A,B)
        # 숫자 갯수의 조합을 모두 traverse. backtracking
        def dfs(first, second, sum, mul):
            if sum < mul or any(e<0 for e in first):
                return 0
            ans = sum if sum == mul else 0
            for i in range(len(B)):
                first[i] -= 1
                second[i] += 1
                ans = max(ans, dfs(first, second, sum-A[i], mul*A[i]))
                second[i] -= 1
                first[i] += 1
            return ans

        ans = dfs(B, [0]*len(B), sum(A[i]*B[i] for i in range(len(A))), 1)

        print("Case #%d:" % T, ans)

def solution2():
    """
    sum = mul
    sum maximum 5 * 10^17 < 2^68 = mul
    계산해봐야 하는 범위는 총합에서 가장 큰수가 mul로 넘어가면서 빠지게되는 합.
    ceil(log가장큰수(총합)) * 가장큰수
    
    PASS!!!
    """
    def checkPossible(full_sum, X, A):
        """
            X이 결과값이 되어야 하는데, 이 값을 소인수 분해한 소인수들의 총합이 diff와 같으면 ok.
        """
        diff = full_sum - X
        for k, v in A:
            # 소인수 분해하면서 가능한지 체크
            n = 0
            while X % k == 0:
                X //= k
                n += 1
                diff -= k
                if n > v or diff < 0:
                    return False
        return X == 1 and diff == 0

    def solve():
        N = int(input())
        A = list(list(map(int, input().split())) for _ in range(N))
        full_sum = sum(a*n for a, n in A)
        max_val = A[-1][0]
        X = math.ceil(math.log(full_sum, max_val)) * max_val
        for s in range(full_sum, max(1, full_sum-X), -1):
            if checkPossible(full_sum, s, A):
                return s
        return 0

    for T in range(1,1+int(input())):
        ans = solve()
        print("Case #%d:" % T, ans)

solution2()