# 문제 설명 : 최소의 점프로 끝에 도달하기. 항상 끝에 도달할 수 있다.

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Greedy하게  jump.
        현재 위치에서 이동할 수 있는 범위 내에서 가장 멀리 갈 수 있는 인덱스를 선택함. 그 횟수를 구하면 됨.
                
        O(N)/O(1)
        """
        N = len(nums)
        ans, i, last = 0, 0, 0
        while i < N-1:
            ans += 1
            i_ = i
            for j in range(i, last+1):
                if j+nums[j] >= N-1:
                    return ans
                i_ = max(i_, j+nums[j])
            i, last = last+1, i_
        return ans