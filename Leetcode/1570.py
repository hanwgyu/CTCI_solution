# 대부분 0이기 때문에 0이 아닌 부분만 idx로 저장하면 된다.

class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {i: n for i, n in enumerate(nums) if n != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(vec.d[i]*n for i, n in self.d.items() if i in vec.d)