# 각 알파벳들의 갯수만 똑같으면 Operation 1번으로 바꿀수 있음.
# 각 알파벳들의 종류와 갯수 조합만 똑같으면 Operation 2번으로 바꿀수 있음.
# Time : O(NlogN), Space: O(1)


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a1, a2 = [0 for _ in range(26)], [0 for _ in range(26)]
        s = set()
        for c in word1:
            s.add(c)
            a1[ord(c) - ord("a")] += 1
        for c in word2:
            a2[ord(c) - ord("a")] += 1
            if c not in s:
                return False
        a1.sort()
        a2.sort()
        return a1 == a2
