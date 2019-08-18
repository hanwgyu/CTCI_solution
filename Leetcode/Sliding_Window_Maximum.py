# Solution 3 : Use Stack. Stack 마지막 원소와 비교해 값이 커지면 작은 값들을 지우고 저장 작아지면 그냥 저장. 
# 0을 output에 저장할 max값의 idx으로 두다가, 해당 원소가 window 범위에 속하지 않으면 idx를 증가시킴. 
# Time : O(N), Space : O(N)

# Solution 1, 2: Use Heap. Time : O(NlogN), Space : O(N)

class Solution:
    def maxSlidingWindow_3(self, nums: List[int], k: int) -> List[int]:
        stack,save_idx, output = [], 0, []
        for i in range(len(nums)):
            while stack and stack[-1][0] < nums[i]:
                stack.pop()
            stack.append((nums[i], i))
            save_idx = min(save_idx, len(stack)-1)
            if i >= k-1:
                while stack[save_idx][1] < i-k+1:
                    save_idx += 1
                output.append(stack[save_idx][0])
        return output
    
    def maxSlidingWindow_2(self, nums: List[int], k: int) -> List[int]:
        a, output = [], []
        for i in range(len(nums)):
            heapq.heappush(a, (-nums[i], i))
            if i < k-1:
                continue
            while a[0][1] <= i-k:
                heapq.heappop(a)
            output.append(-a[0][0])
        return output
            
        
    def maxSlidingWindow_1(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None
        a, output = [], [None for _ in range(len(nums)-k+1)]
        for i in range(len(nums)):
            heapq.heappush(a, (-nums[i], i))
            
        while a:
            val = heapq.heappop(a)
            for i in range(max(val[1]+1-k, 0), min(val[1] , len(output)-1)+1):
                if not output[i]:
                    output[i] = -val[0]
        return output
