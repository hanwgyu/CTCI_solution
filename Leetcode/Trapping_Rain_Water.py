# Solution 1: 가장 높은 Wall을 찾음. 양끝에서 시작해서, 가장 높은 wall에 다다를때까지 계산.
# 지금까지 마주친 가장 높은 블록을 Wall로 설정하여, 새로운 블록을 마주칠때마다 차이값을 계산하여 더함.
# 현재 Wall과 같은 높이거나 더 높은 블록을 마주칠때마다 Wall을 업데이트.
# Time complexity : O(N), Space complexity : O(1)

# Solution 3: Stack. 높이가 낮아지는 stack을 만듬. stack에는 idx를 저장.
# 높이가 높아질경우, 낮은 원소들을 하나씩 pop하면서 각 원소에 대한 물양을 계산해나감. (idx 차이 계산시 st에 저장된 가장 마지막과의 차이를 구해야함)
# Time complexity : O(N), Space complexity : O(1)


class Solution:
    def trap_3(self, height: List[int]) -> int:
        st, ans = [], 0
        for i, h in enumerate(height):
            while st and height[st[-1]] < h:
                h_b = height[st.pop()]
                if not st:
                    break
                ans += (i - st[-1] - 1) * (min(height[st[-1]], h) - h_b)
            st.append(i)
        return ans

    def trap_2(self, height: List[int]) -> int:
        l, r, l_max, r_max, ans = 0, len(height) - 1, 0, 0, 0
        while l < r:
            if height[l] < height[r]:
                l_max = max(l_max, height[l])
                ans += l_max - height[l]
                l += 1
            else:
                r_max = max(r_max, height[r])
                ans += r_max - height[r]
                r -= 1
        return ans

    def trap_1(self, height):
        if not height:
            return 0

        # Find index of maximum value
        highest_wall = height.index(max(height))

        total_water = 0
        # left-to-right
        wall_height = 0
        for i in range(highest_wall):
            wall_height = max(wall_height, height[i])
            total_water += wall_height - height[i]

        # right-to-left
        wall_height = 0
        for i in reversed(range(highest_wall, len(height))):
            wall_height = max(wall_height, height[i])
            total_water += wall_height - height[i]

        return total_water
