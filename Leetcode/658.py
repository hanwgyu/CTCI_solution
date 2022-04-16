class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        슈퍼 하드한 Binary Search..
        arr[m]과 범위 다음값인 arr[m+k]를 비교한다.
        arr[m]이 더 크면 m을 한칸 오른쪽으로 이동할 수 있다는 의미.
        arr[m]이 더 작으면 왼쪽으로 이동.
        
        """
        l, r = 0, len(arr)-k-1
        while l <= r:
            m = (l+r)//2
            if x- arr[m] > arr[m+k]-x:
                l = m+1
            else:
                r = m-1
        return arr[l:l+k]
