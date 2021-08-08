# 고민 1: DP. 특정 student, mentor의 compatibility score를 저장해놓음.
# 모든 combination에 대해 반복해서 계산
# Time : O(N!M), Space : O(N^2)

from itertools import permutations

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        dp = defaultdict(int)

        # 모든 student, mentor의 compatibility score를 저장
        for i, s in enumerate(students):
            for j, m in enumerate(mentors):
                score = 0
                for k in range(len(s)):
                    if s[k] == m[k]:
                        score += 1
                dp[(i,j)] = score

        ans = 0
        # 모든 combination에 대해 반복해서 계산
        for permutation in permutations([i for i in range(len(students))]):
            s = sum([dp[(i,j)] for i, j in enumerate(permutation)])
            ans = max(ans, s)
        return ans
