# Solution 1 : 모든 원소들이 다르므로 pieces의 가장 첫번째 원소들만 hash에 저장해놓고 arr의 처음부터 진행하면서 동일한 원소를 찾음.
# Time : O(M), Space : O(N) (M: arr의 크기, N : pieces의 크기)


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {}
        for i, p in enumerate(pieces):
            d[p[0]] = i
        i = 0
        while i < len(arr):
            if arr[i] in d:
                for e in pieces[d[arr[i]]]:
                    if e != arr[i]:
                        return False
                    i += 1
            else:
                return False
        return True
