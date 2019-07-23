#Time complexity : O(N), Space complexity : O(1)
class Solution(object):
    def trap(self, height):
        #Solution : 가장 높은 Wall을 찾음. 양끝에서 시작해서, 가장 높은 wall에 다다를때까지 올라가거나 같은 높이의 WALL을 마주칠때마다 값을 즉시 계산.
        
        if not height:
            return 0
        
        #Find index of maximum value
        highest_wall = height.index(max(height))
 
        total_water = 0
        #left-to-right
        wall_height = 0
        for i in range(highest_wall):
            wall_height = max(wall_height, height[i])
            total_water += (wall_height - height[i])
    
        #right-to-left
        wall_height = 0
        for i in reversed(range(highest_wall, len(height))):
            wall_height = max(wall_height, height[i])
            total_water += (wall_height - height[i])
        
        return total_water