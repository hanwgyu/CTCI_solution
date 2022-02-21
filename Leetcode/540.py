class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        binary search를 하되, 같은 값이 [짝수, 홀수]에 있는지 [홀수, 짝수] 에 있는지로 오른쪽, 왼쪾으로 이동.
        """
        N = len(nums)
        l, r = 0, N-1
        while l <= r:
            m = (l+r) //2
            if (m+1 == N or (m+1 < N and nums[m] != nums[m+1])) and (m == 0 or (m-1 >= 0 and nums[m] != nums[m-1])):
                return nums[m]
            elif m+1 < N and nums[m] == nums[m+1]:
                if m%2 == 0:
                    l = m+1
                else:
                    r = m-1
            else:
                if m%2 == 0:
                    r = m-1
                else:
                    l = m+1
        return -1
            
        
        
    def singleNonDuplicate1(self, nums: List[int]) -> int:
        """
        XOR 이용
        O(N) / O(1)
        """
        ans = 0
        for n in nums:
            ans ^= n
        return ans