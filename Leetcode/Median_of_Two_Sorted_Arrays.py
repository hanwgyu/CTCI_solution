# 처음 생각한 아이디어는 포인터 두개를 두고 동시에 움직이면서 Partition을 정확하게 절반씩 나누는 방법을 생각했는데, 이렇게되면 log() Time complexity가 나오지 않음.

# Solution : 포인터 하나만 움직이고, 다른 포인터는 무조건 Partition을 절반으로하는 지점을 찾아서 계산하는 방식을 구현.
# 포인터 크기를 idx의 두배값으로 잡아, 원소 갯수가 홀수/짝수일때에 대한 예외처리를 줄임 
# Time : O(log(min(M,N))), Space :O(1)  

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 < n2:
            return self.findMedianSortedArrays(nums2, nums1)
        l, r = 0, 2*n2
        
        while l <= r:
            m2 = (l + r)//2
            m1 = n1 + n2 - m2
         
            L1 = nums1[(m1-1)//2] if m1 > 0 else float('-inf')
            R1 = nums1[m1//2] if m1 < 2*n1 else float('inf')
            L2 = nums2[(m2-1)//2] if m2 > 0 else float('-inf')
            R2 = nums2[m2//2] if m2 < 2*n2 else float('inf')
            if R1 < L2:
                r = m2 - 1
            elif R2 < L1:
                l = m2 + 1
            else: #  L1와 L2 를 기준으로 오른쪽 파티션보다 값이 작은 절반 원소들로 구성되었음.
                return (max(L1, L2) + min(R1, R2)) / 2
        return -1   
            
