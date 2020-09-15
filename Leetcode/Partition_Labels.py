# Solution : 각 letter가 마지막으로 나오는 index를 저장.
# Time : O(N), Space: O(1)


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {c: i for i, c in enumerate(S)}
        letters = set()
        ret = []
        l = 0
        for i, c in enumerate(S):
            if i == d[c]:
                if c in letters:
                    letters.remove(c)
            else:
                letters.add(c)
            l += 1
            if len(letters) == 0:
                ret.append(l)
                l = 0
        return ret
