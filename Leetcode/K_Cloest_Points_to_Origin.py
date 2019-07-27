class Solution(object):
    #Time Complexity : O(NlogN), Space Complexity : O(N)
    def kClosest(self, points, K):
        d = []
        for i in range(len(points)):
            d.append((points[i][0]**2 + points[i][1]**2, i)) # (distance, index)
        
        d.sort(key = lambda e : e[0])
        
        ans = []
        for i in range(K):
            ans.append(points[d[i][1]])
        return ans
        
        
