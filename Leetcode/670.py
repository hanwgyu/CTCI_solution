class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        앞에서부터 가장 큰수 순서대로 배열되야함.
        1~9까지 index의 가장 마지막 위치를 저장함. 
        """
        A = list(map(int, str(num)))
        last = {x:i for i, x in enumerate(A)}
        
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if d in last and last[d] > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(list(map(str, A))))
        return num