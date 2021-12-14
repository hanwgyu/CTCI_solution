# REMIND : 
# 전혀 몰라서 풀이봤음.

def memorization(func):
    memo = dict()
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return wrapper

class Solution:
    @memorization
    def encode(self, s: str) -> str:    
        """
        encode가 최선의 방법을 리턴한다고 가정하고, 큰 s를 짧은 s들로 쪼개 encode를 다시 계산하고 합치는 방식의 풀이.
        case 1: s
        case 2: s[:i] + s[i:]
        case 3: s 전체를 3개 이상으로 쪼개는 방법 -> s+s 에서 s가 가장 처음 나오는 곳을 찾음
            ex) ababab => abababababab => ab[ababab]abab => index 2를 리턴. s[:index]가 가장 작은 공통 문자.
        """
        N = len(s)
        # case 3
        i = (s+s).find(s, 1) # (s+s)[1:]에서 substring s를 찾음
        s3 = f'{N // i}[{self.encode(s[:i])}]' if i < N and i != -1 else s
        #case 2
        s2 = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1, N)]
        return min([s, s3]+s2, key=len)