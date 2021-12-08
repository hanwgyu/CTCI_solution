# 모든 회전 가능한 숫자중에 rotate해도 동일한 값을 가지는 숫자들의 갯수를 뺸다.
# 모든 회전 가능한 숫자 : 0,1,6,8,9 로 구성가능한 숫자
# 동일한 값을 가지려면 : 중간을 기준으로 대칭 되는 숫자. (0,0) (1,1) (6,9) (8,8)

# backtracking으로 돌리는게 제일 편하다..

class Solution:
    def confusingNumberII(self, n: int) -> int:
        """
        특정 숫자로 시작하는 값에서 시작해 오른쪽에 digit을 붙이고, 모든 rotation 값들을 방문하면서 체크 진행. 
        """
        valid = [0, 1, 6, 8, 9]
        rotate = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        def backtrack(origin: int, rotated: int, depth: int = 1) -> int:
            if not origin or origin > n:
                return 0
            ans = 0
            if origin != rotated:
                ans += 1
            for d in valid:
                ans += backtrack(origin*10+d, pow(10, depth)
                                 * rotate[d]+rotated, depth+1)
            return ans

        return sum(backtrack(d, rotate[d]) for d in valid)
