# 고민 1 : sorting 해서 비교.
# Time : O(NlogN), Space : O(N)

# 고민 2 : height 범위가 100까지이므로 frequnecy를 저장해서 비교.
# Time : O(1), Space : O(1)

class Solution:
    def heightChecker_1(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

    def heightChecker_2(self, heights: List[int]) -> int:
        freq = [0]*101
        for h in heights:
            freq[h] += 1
        cur_h = 1
        ans = 0
        for h in heights:
            while freq[cur_h] == 0:
                cur_h += 1
            if cur_h != h:
                ans += 1
            freq[cur_h] -= 1
        return ans
