# abs가 작은 순서대로 iterate하면서 갯수를 체크.
# Time : O(NlogN), Space: O(N)

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        for x in sorted(arr, key=abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1
        return True
