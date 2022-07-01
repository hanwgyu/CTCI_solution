"""
Segment Tree!!!!!

https://www.youtube.com/watch?v=ZBHKZF5w4YU 이 유투브 참고했음.

"""

class NumArray:

    def __init__(self, nums: List[int]):
        self.N = len(nums)
        self.nums = nums
        self.segment_tree = [0 for _ in range(4*self.N)] # 2*N보다 더 넉넉하게 해야함!.
        
        def createTree(low:int, high:int, pos:int):
            if low == high:
                self.segment_tree[pos] = self.nums[low]
                return
            mid = (low+high)//2
            createTree(low, mid, 2*pos+1)
            createTree(mid+1, high, 2*pos+2)
            self.segment_tree[pos] = self.segment_tree[2*pos+1] + self.segment_tree[2*pos+2]
            
        createTree(0, self.N-1, 0)

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        def updateInTree(low, high, pos, index):
            if index < low or high < index:
                return
            if low == high:
                self.segment_tree[pos] = self.nums[low]
                return 
            mid = (low+high) // 2
            updateInTree(low, mid, 2*pos+1, index)
            updateInTree(mid+1, high, 2*pos+2, index)
            self.segment_tree[pos] = self.segment_tree[2*pos+1] + self.segment_tree[2*pos+2]
        updateInTree(0, self.N-1, 0, index)
            
    def sumRange(self, target_low: int, target_high: int) -> int:
        def sumRangeInTree(low, high, pos, target_low, target_high) -> int:
            if target_low <= low and high <= target_high: # total overlap
                return self.segment_tree[pos]
            elif target_high < low or high < target_low: # no overlap
                return 0
            mid = (low+high)//2
            return sumRangeInTree(low, mid, 2*pos+1, target_low, target_high) + sumRangeInTree(mid+1, high, 2*pos+2, target_low, target_high)
        return sumRangeInTree(0, self.N-1, 0, target_low, target_high)        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
