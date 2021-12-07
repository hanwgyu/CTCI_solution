# 문제 요약 : S의 연속된 substring 중 s2를 subsequence로 포함하는 가장 짧고 왼쪽에 있는 문자를 리턴

# 일단 첫글자랑 끝글자는 똑같아야 가장 짧은것.
# 왼쪽부터 시작하면서 동일한 첫글자와 오른쪽부터 시작하면서 동일한 끝글자를 가지는 substring을 최대한 작은 크기로 줄여나가보자.

# subsequence인지 찾는 방법? 그냥 모두 비교해야할듯.? O(M+N)

# 결국 그냥 다 찾는건데, 최대한 깔끔하게 잘 찾는게 중요한 문제.
# 앞에서부터 찾아서 endpoint를 찾은후, startpoint를 개선해나아감.


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        def findFromStart(s) -> int:  # return endpoint
            t = 0
            while s < len(S):
                if S[s] == T[t]:
                    t += 1
                    if t == len(T):
                        break
                s += 1
            return s if t == len(T) else None

        def findFromEnd(s) -> int:  # return startpoint
            t = len(T) - 1
            while t >= 0:
                if S[s] == T[t]:
                    t -= 1
                    if t == -1:
                        break
                s -= 1
            return s if t == -1 else None

        s, ans = 0, ''
        while s < len(S):
            end = findFromStart(s)  # Find end-point of subsequence
            if end is None:
                break

            start = findFromEnd(end)  # Improve start-point of subsequence
            if ans == '' or end - start + 1 < len(ans):  # Track min length
                ans = S[start:end+1]
            s = start + 1  # Start next subsequence search
        return ans
