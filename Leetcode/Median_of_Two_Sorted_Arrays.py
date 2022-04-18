# 처음 생각한 아이디어는 포인터 두개를 두고 동시에 움직이면서 Partition을 정확하게 절반씩 나누는 방법을 생각했는데, 이렇게되면 log() Time complexity가 나오지 않음.

# Solution : 포인터 하나만 움직이고, 다른 포인터는 무조건 Partition을 절반으로하는 지점을 찾아서 계산하는 방식을 구현.
# 포인터 크기를 idx의 두배값으로 잡아, 원소 갯수가 홀수/짝수일때에 대한 예외처리를 줄임
# Time : O(log(min(M,N))), Space :O(1)


"""
210822

구하고자 하는 것은 sorted된 array의 갯수로써 중간이 되는 지점.
일단 binary search를 적용하기 위해서는.. 공동의 범위 l, r를 두고, m1을 구한후, m2는 합친 갯수를 정확히 절반으로 나누는 곳으로 이동해야함.
m1, m2를 이동해나아가면서 값으로서 m1,m2 를 기준으로 왼쪽 파티션의 값들이 오른쪽 파티션 값들보다 항상 작아야함.

범위를 잡는게 까다로운 부분.
m1의 범위는 작은 원소를 가진 갯수의 범위 +- 1 로 잡고, 최대 범위를 벗어나면 값을 float('inf'), float('-inf')로 처리함.
"""

"""
l, r, m2를 nums2 내 범위로 잡고, (m2는 원하는 위치의 다음값)
m1 은 합친 어레이의 갯수를 정확히 반으로 나누는 위치를 계산.
l2, r2 은 m2-1, m2 위치의 값으로 설정.
l1, r1 은 m1-1, m1 위치의 값으로 설정.

r2 < l1 이면 아직 m2가 충분히 오른쪽으로 이동하지 않았으므로 l = m2+1으로 이동,
r1 < l2 이면 m2가 너무 오른쪽으로 이동했으므로 r = m2-1로 이동.
두 조건을 모두 만족하지 않으면 l1,r1 과 l2,r2가 겹치는 부분이 있으므로 정상적으로 절반으로 나누게 된 것이고, 
짝수와 홀수 갯수를 구분해 결과를 리턴.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M, N = len(nums1), len(nums2)
        if M < N:
            return self.findMedianSortedArrays(nums2, nums1)
        l, r = -1, N
        is_even = ((M + N) % 2) == 0
        while l <= r:
            m2 = (l+r)//2
            m1 = (M+N+1)//2-m2
            l1 = float('inf') if m1-1 > M-1 else (float('-inf') if m1-1 < 0 else nums1[m1-1])
            r1 = float('inf') if m1 > M-1 else (float('-inf') if m1 < 0 else nums1[m1])
            l2 = float('inf') if m2-1 > N-1 else (float('-inf') if m2-1 < 0 else nums2[m2-1])
            r2 = float('inf') if m2 > N-1 else (float('-inf') if m2 < 0 else nums2[m2])
            if r2 < l1:
                l = m2 + 1
            elif l2 > r1:
                r = m2 - 1
            else:
                if not is_even:
                    return max(l1,l2)
                else:
                    return (max(l1,l2) + min(r1,r2))/2
        return -1

class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 < n2:
            return self.findMedianSortedArrays(nums2, nums1)
        l, r = 0, 2 * n2

        while l <= r:
            m2 = (l + r) // 2
            m1 = n1 + n2 - m2

            L1 = nums1[(m1 - 1) // 2] if m1 > 0 else float("-inf")
            R1 = nums1[m1 // 2] if m1 < 2 * n1 else float("inf")
            L2 = nums2[(m2 - 1) // 2] if m2 > 0 else float("-inf")
            R2 = nums2[m2 // 2] if m2 < 2 * n2 else float("inf")
            if R1 < L2:
                r = m2 - 1
            elif R2 < L1:
                l = m2 + 1
            else:  #  L1와 L2 를 기준으로 오른쪽 파티션보다 값이 작은 절반 원소들로 구성되었음.
                return (max(L1, L2) + min(R1, R2)) / 2
        return -1
