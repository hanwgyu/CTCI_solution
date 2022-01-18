"""
    Append Sort
"""
import sys
import bisect
import collections
import itertools
import math

T = int(input())


"""
    점점 커지게 해야하는데, 문자를 추가할때 최대한 작은 문자로 쓴다. Greedy.

    추가하는 숫자를 매번 구해가면서 계산해야 하는지, 아니면 그냥 좀더 최적화 할 수 있나? 
    => 매번 계산해야 한다. 123, 11, 1101 과 같은 경우  11-> 1100으로 바꿀때만 답이 2고, 1100보다 커지면 3이된다.

    아래와 같이 케이스를 나눠서 생각한다.
    B, A
    1) 123, 12 와 같이 문자가 겹치는 경우: 12->124 (B+1)
    1-1) 123, 123 과 같이 똑같은 경우 : 1230 (A*10)
    1-2) 19, 1 처럼 차이나는 부분이 모두 9인 경우 : 100 (A+10*(len(B)-len(A)+1))
    2) 123, 11 과 같이 더 작은 경우 : 11->1100 (A+10*(len(B)-len(A)+1))
    3) 123, 13 과 같이 더 큰 경우 : 130 (A+10*(10,len(B)-len(A)))
    4) 0인 경우 : (B+1) 
"""

"""
후기)
    와 너무 어렵다. 2시간 넘게 걸림....
    어떤 케이스에 틀리는지도 모르겠고 걍 계속 틀림. 예외처리를 정말 오지게 한번에 생각해서 해야한다.
    모든 경우의 수를 머릿속으로 생각할 수 있어야한다.

*** 문자를 비교하면 앞글자부터 알파벳 순으로 비교함.
"""

for testCase in range(1, T + 1):
    # SOLVE
    _ = input()
    nums = input().split()
   
    ans = 0
    for i in range(len(nums)-1):
        B, A = nums[i], nums[i+1]
        if len(B) < len(A):
            continue

        if A == "0":
            nums[i+1] = str(int(B)+1)
            ans += len(B)
            continue

        if B[0:len(A)] == A and len(A)==len(B):
            ans += 1
            nums[i+1]= A+'0'

        if B[0:len(A)] == A and len(A) < len(B):
            if set(B[len(A):]) == set('9'):
                ans += len(B)-len(A)+1
                nums[i+1]= A+'0'*(len(B)-len(A)+1)
            else:
                ans += len(B)-len(A)
                nums[i+1] = str(int(B)+1)

        if B[0:len(A)] > A:
            ans += len(B)-len(A)+1
            nums[i+1] = A+'0'* (len(B)-len(A)+1)

        if B[0:len(A)] < A:
            ans += len(B)-len(A)
            nums[i+1] = A+'0'* (len(B)-len(A))
    print("After change: ", nums) # REMOVE
    # ANSWER
    print("Case #" + str(testCase) + ": " + str(ans))