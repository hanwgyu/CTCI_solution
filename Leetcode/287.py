""" 
세가지 다 천재적인 방법.
"""

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

    def findDuplicate(self, nums: List[int]) -> int:
        """
        특정 숫자와 그 숫자에 해당하는 인덱스의 숫자를 linked list로 연결한다고 생각하면,
        겹치는 부분에서 cycle이 시작되는 형태가 된다.
        cycle의 head 는 항상 nums[0]. 0을 가리키는 곳은 없다.
        
        cycle 시작하는 부분을 구하는건 https://leetcode.com/problems/linked-list-cycle-ii/ 이 문제와 동일하게 푼다.

        O(N) / O(1) 와우... 천재인가?
        """
        fast = slow = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                slow = nums[0]
                while fast != slow:
                    slow = nums[slow]
                    fast = nums[fast]
                return fast
