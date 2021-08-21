# Time : O(logN), Space : O(1)
# 범위 설정하는 것이 상당히 까다로움. 여러번 시행착오를 거쳐 해답을 찾아냈음.


# m을 l, r과 비교하면서 rotated된걸을 확인해서 진행
# <=로 할지 <로 할지, r = m 으로할지, r = m-1로 할지 매우 어려움. 정형화 되어있는게 아니라 로직에 따라 결정을 해야함.
# 이 경우에는 매우우우우우어렵다..........ㅠㅠ

# Solution 2 :
# if 왼쪽 부분이 monotonically increasing => pivot이 오른쪽에 있다
#   if left <= target < mid -----> 오른쪽 절반 날림
#   else  -----> 왼쪽 절반 날림
# else 오른쪽 부분이 monotonically increasing => pivot이 왼에 있다
#   if mid < target <= right ---> 왼쪽 절반 날림
#   else ----> 오른쪽 절반 날림

# Solution 3 : 일반 binary search하는 것처럼 동작시키기 위해 target과 nums[m]값이
# 위치하는 수열이 다른 경우, inf, -inf값으로 설정해 search를 동작시킨다.


class Solution:
    def search_3(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            num = (
                nums[m]
                if (target < nums[0]) == (nums[m] < nums[0])
                else (float("-inf") if target < nums[0] else float("inf"))
            )
            if num < target:
                l = m + 1
            elif num > target:
                r = m - 1
            else:
                return m
        return -1

    def search_2(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]: # 이부분을 < 로하면 '[3,1], 1'을 통과 못함... 이게 까다로운 부분이다.
                # m이 //2로 계산하기 때문에 원소 갯수가 2개로 작으면 l==m이 되고,
                # 조건문이  r= m-1로 진행될경우  그다음에 바로 while문을 빠져나온다. 근데 이러면 1인 부분을 체크할 수 없다.
                # 최대한 l을 변경하는 방식으로 진행되야 while문을 끝내지 않고 체크를 한번 더할 수 있다.
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

    def search_1(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # pivot이 존재하지 않는 경우
            if nums[l] < nums[r]:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            # pivot이 m 뒤쪽에 존재하는 경우
            elif nums[l] < nums[m]:
                if nums[m] < target or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # pivot이 m 앞쪽에 존재하는 경우
            elif nums[l] > nums[m]:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            # l과 m이 같은 경우
            else:
                l = m + 1
        return l if nums and nums[l] == target else -1
