class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        mh = 0
        for i in reversed(range(len(heights))):
            if mh < heights[i]:
                ans.append(i)
            mh = max(mh, heights[i])
        return ans[::-1]