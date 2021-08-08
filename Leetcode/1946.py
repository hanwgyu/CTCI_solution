# Time : O(N), Space : O(N)

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        a = list(num)
        start = False
        for i, c in enumerate(a):
            c = int(c)
            if change[c] > c:
                a[i] = str(change[c])
                start = True
            elif start and change[c] < c:
                break
        return "".join(a)
