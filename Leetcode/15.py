class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sorting 한후 하나의 index에 대해 Two pointer 문제로 해결
        (167번 문제 참고)

        O(N^2) / O(1)
        """
        N, res = len(nums), []
        nums.sort()
        for i in range(N-2):
            # 중복되는 정답 패스하기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, N-1
            while l < r:
                if -nums[i] > nums[l]+nums[r]:
                    l += 1
                elif -nums[i] < nums[l]+nums[r]:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    # 중복되는 정답 패스하기
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l, r = l+1, r-1
        return res