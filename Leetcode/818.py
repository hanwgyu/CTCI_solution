# 문제 해설 : A, R에 따라 차의 속도가 변함.
# A는 현재 속도대로 이동후 속도를 2배, R은 -1 or 1로 속도를 변경함.
# target position에 도달하게 되는 최소의 변경 횟수를 구할것.

# 현재 위치에 따른 값을 visited로 저장하고, bfs로 구해나감?, 
# R은 최대 2번을 연속으로 쓰게.

# 2진수를 연속으로 빼고 더하는걸 고려.
# 1000을 만드려면 111 + 1 => AAA RR A
# 1011 = 1111 - 11 + 1 (AAAA R AA RR A) or 111 + 1 + 11 (AAA RR A RR AA)
# + 는 RR, -는 R, 나머지 연속된 1은 A로 구성. 가장 작은 갯수를 구하자.

# 1) queue + visited 로 instruction이 작은 순서대로, BFS로 처리하면서 진행. 

# 2) DP. (1111 - 세글자) or (111 + 세글자) 두경우를 계산. 
# REMIND : 진짜 어렵고 중요하다. !!! (111+ 세글자) 뿐만 아니라 (111 - 1 + 세글자)까지 고려해서 계산해야 모든 케이스를 고려할 수 있다.


class Solution:
    def racecar_3(self, target: int) -> int:
        """
        2번 방법을 개선. 필요한 숫자만 계산하게.
        """
        dp = {0:0}
        def find(t):
            if t in dp:
                return dp[t]
            n = t.bit_length()
            if 2**n - 1 == t:
                dp[t] = n
            else:
                dp[t] = find(2**n - 1 - t) + n + 1
                for m in range(n - 1):
                    dp[t] = min(dp[t], find(t - 2**(n - 1) + 2**m) + n + m + 1)
            return dp[t]
        return find(target)

        
    
    def racecar_2(self, target: int) -> int:
        pow2 = target.bit_length() + 1
        
        dp = [float('inf') for _ in range(pow(2,pow2))] #마지막 연산자 (+, -)
        for n in range(1, pow2):
            dp[pow(2, n)-1] = n
        for n in range(1, pow2):
            for i in range(pow(2, n-1), pow(2, n)):
                # (1111 - 세글자)
                dp[i] = min(dp[i], n+1+dp[pow(2, n)-1-i])
                # (111 + 세글자) (가운데가 없어도 +를 만드는데 RR로 결국 뒷부분과 계산식이 똑같음.) or (111 - 1 + 세글자) or (111 - 11 + 세글자)
                for m in range(n):
                    dp[i] = min(dp[i], n-1+1+dp[i-(pow(2, n-1)-1)+(pow(2,m)-1)]+1+m)
                if i == target:
                    return dp[i]
         
    def racecar_1(self, target: int) -> int:
        # 최대 target의 2진수 최대값까지만 계산.
        pow2, temp = 0, target
        while temp:
            temp //= 2
            pow2 += 1

        visited = set()
        q = deque([(0,1,0)])
        while q:
            pos, speed, n  = q.popleft()
            if pos == target:
                return n
            if pos in visited or pos < 0 or pos >= pow(2, pow2):
                continue
            q.append((pos+speed, speed*2, n+1))
            q.append((pos, 1 if speed < 0 else -1, n+1))
        return -1
            