class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        In-place

        O(N) / O(1)
        """
        a = nums[0]
        while a != nums[a]:
            temp = nums[a]
            nums[a] = a
            a = temp
        return a
    
    def findDuplicate(self, nums: List[int]) -> int:
        """
        특정 숫자 m보다 작은 원소의 갯수가 m개 이상이면 그보다 작은 숫자에 겹치는 숫자가 있다는 뜻. 
        (m-1개 이하이면 그와 같거나 큰 숫자에 정답이 있다)
        
        Binary Search로 해결.
        
        미친 솔루션. 이렇게 정답 자체를 가정하고, 범위를 줄여가면서 푸는 테크닉을 알고 있어야함.
        
        O(NlogN) / O(1)
        """
        ans = 1
        l, r = 1, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            n_smaller = sum(1 for n in nums if n < m)
            if n_smaller >= m:
                r = m-1
            else:
                ans = m
                l = m+1
        return ans
