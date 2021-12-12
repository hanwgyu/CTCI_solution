# 모든 경우를 체크. binary search 이용해 서치 비용을 줄임

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # start pos를 제외.
        temp = []
        start_amount = 0
        for a, b in fruits:
            if a == startPos:
                start_amount = b
                continue
            temp.append([a, b])
        fruits = temp
        N = len(fruits)
        print(fruits, N)

        start_idx = bisect.bisect(fruits, [startPos, 0])
        l, r = [], []
        # Left
        acc = 0
        for i in reversed(range(0, start_idx)):
            pos, amount = fruits[i]
            acc += amount
            l.append((startPos - pos, acc))
        # Right
        acc = 0
        for i in range(start_idx, N):
            pos, amount = fruits[i]
            acc += amount
            r.append((pos - startPos, acc))

        ans = 0
        # Left -> Right
        for length, acc in l:
            if length <= k:
                i = bisect.bisect_right(r, (k-2*length, float('inf')))
                if i > 0:
                    acc += r[i-1][1]
                ans = max(acc, ans)
            else:
                break
        # Right -> Left
        for length, acc in r:
            if length <= k:
                i = bisect.bisect_right(l, (k-2*length, float('inf')))
                if i > 0:
                    acc += l[i-1][1]
                ans = max(acc, ans)
            else:
                break
        return ans + start_amount
