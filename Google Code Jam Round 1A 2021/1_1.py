"""
다른 사람 풀이.
겁나리 신기하다 ㅋ 그냥 정말 간단하게 다 체크해버림.
"""

for T in range(1,1+int(input())):
  N = int(input())
  A = list(map(int,input().split()))
  cur = A[0]
  ans = 0
  for x in A[1:]:
    for n in range(0,1000):
      l = x * 10**nㄹㄹ
      r = x * 10**n + (10**n - 1)
      if r <= cur:
        continue
      if cur < l:
        cur = l
        ans += n
        break
      if l <= cur < r:
        cur += 1
        ans += n
        break
      raise Exception("??")
  
  print("Case #%d:" % T, ans)