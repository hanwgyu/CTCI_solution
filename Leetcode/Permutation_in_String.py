# Solution 1 : Time : O(l1+l2), Space : O(1)

# Solution 2 : Solution 1에서 array check를 줄임.
# Time : O(l1+l2), Space : O(1)


class Solution:
    def checkInclusion_2(self, s1: str, s2: str) -> bool:
        def index(s: str) -> int:
            return ord(s) - ord("a")

        if len(s1) > len(s2):
            return False
        N = 26
        a1, a2 = [0] * N, [0] * N
        for i in range(len(s1)):
            a1[index(s1[i])] += 1
            a2[index(s2[i])] += 1
        cnt = 0
        for i in range(N):
            if a1[i] == a2[i]:
                cnt += 1
        for i in range(len(s1), len(s2)):
            if cnt == N:
                return True
            l, r = index(s2[i - len(s1)]), index(s2[i])
            a2[l] -= 1
            if a2[l] + 1 == a1[l]:
                cnt -= 1
            elif a2[l] == a1[l]:
                cnt += 1
            a2[r] += 1
            if a2[r] - 1 == a1[r]:
                cnt -= 1
            elif a2[r] == a1[r]:
                cnt += 1
        return cnt == N

    def checkInclusion_1(self, s1: str, s2: str) -> bool:
        def index(s: str) -> int:
            return ord(s) - ord("a")

        if len(s1) > len(s2):
            return False
        a1, a2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            a1[index(s1[i])] += 1
            a2[index(s2[i])] += 1
        if a1 == a2:
            return True
        for i in range(len(s1), len(s2)):
            a2[index(s2[i - len(s1)])] -= 1
            a2[index(s2[i])] += 1
            if a1 == a2:
                return True
        return False
