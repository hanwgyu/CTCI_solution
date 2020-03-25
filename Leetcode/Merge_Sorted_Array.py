# Solution : 뒤에서부터 넣음.
# Time : O(M+N), Space : O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            a, b = nums1[m-1], nums2[n-1]
            nums1[m+n-1] = max(a, b)
            if a > b: m = m-1
            else: n = n-1
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
