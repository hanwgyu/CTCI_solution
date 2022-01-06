
# 자기 보다 오른쪽에 있는 원소들만 가지고 내림 차순으로 sorting 했을때 오른쪽부터의 index.
# 전체로 합쳐지는 순간에서 왼쪽 원소일 경우에만 남은 오른쪽 배열의 원소 갯수로 값을 업데이트함.
# 오른쪽 원소인 경우에는 이미 오른쪽에 있어서 문제에서 고려하는 케이스가 아니다.
# 첫 index를 저장하여 결과를 구할때 사용.

# REMIND : 천재적인 아이디어. 어려워. mergesort 구현도 pop을 써서 깔끔함.

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        def mergesort(A):
            """
                오름 차순으로 정렬.
            """
            half = len(A) // 2
            if half:
                L, R = mergesort(A[:half]), mergesort(A[half:])
                for i in reversed(range(len(A))):
                    if not R or L and L[-1][1] > R[-1][1]:
                        res[L[-1][0]] += len(R)
                        A[i] = L.pop()
                    else:
                        A[i] = R.pop()
            return A
        mergesort(list(enumerate(nums)))
        return res
        