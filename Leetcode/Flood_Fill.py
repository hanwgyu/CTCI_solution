# Solution : DFS
# Time: O(N), Space: O(N)

from collections import defaultdict
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        originColor = image[sr][sc]
        
        def fill(image: List[List[int]], r: int, c: int, newColor: int):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            if image[r][c] == newColor or image[r][c] != originColor:
                return
            image[r][c] = newColor
            for (x,y) in [(1,0), (-1,0), (0,1), (0,-1)]:
                fill(image, r+x, c+y, newColor)
                
        fill(image, sr, sc, newColor)
        return image
