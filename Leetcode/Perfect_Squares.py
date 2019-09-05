# Solution 1 : DP. 
# Time Limit Exceeded. Time : O(N^2), Space : O(N)

# Solution 2 : BFS. 
# Time : O(N^2), Space : O(N)

class Solution:    
    def numSquares_2(self, n: int) -> int:
        q, depth = {n}, 0
        while q:
            depth += 1
            temp = set()
            for i in q:
                for j in range(1, int(n**0.5+1)):
                    if i == j*j:
                        return depth
                    temp.add(i-j*j)
                q = temp
        return depth
    
    
    def numSquares_1(self, n: int) -> int:
        min_nums = [0]
        for i in range(1, n+1):
            min_num = float('inf')
            for j in range(1, int(i**0.5+1)):
                min_num = min(1 + min_nums[i-j**2], min_num)
            min_nums.append(min_num)
        return min_nums[n]
