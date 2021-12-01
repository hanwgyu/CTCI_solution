# 고민 1: set에 넣어놓고, 있는지 여부를 모두 계산.

# 고민 2: 원소가 n개이므로 i번째 원소의 i번째 비트의 ~을 합친 결과를 리턴
# Time : O(N), Space: O(1)

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join("0" if n[i] == "1" else "1" for i, n in enumerate(nums))

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums[0])
        s = set()
        for n in nums:
            s.add(int(n,2))
        for i in range(2**N):
            if i not in s:
                r = bin(i)[2:]
                return "0"*(N-len(r))+r
        return -1
