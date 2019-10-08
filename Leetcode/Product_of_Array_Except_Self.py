# Time : O(N), Space : O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p, ans, zeros = 1, [], 0
        for num in nums:
            if num != 0 : 
                p *= num
            else:
                zeros += 1
                
        for num in nums:
            if num != 0 and zeros > 0:
                e = 0
            elif num != 0:
                e = p // num
            elif zeros == 1:
                e = p
            else:
                e = 0
            ans.append(e)
        return ans
