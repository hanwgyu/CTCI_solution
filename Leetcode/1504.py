# 고민 1: 특정 포인트마다 i, j 로 늘려가면서 1만 존재하는 사각형을 구함
# Time : O(M^2*N^2), Space : O(1)

# 고민 2: discussion 봄. 범위합을 구하는것은 increasing stack을 이용하는게 유용함!
# Stack. 높이가 높아지는 stack을 만듬. stack에는 idx를 저장.
# 높이가 낮아질경우, 낮은 원소들을 하나씩 pop하면서 각 원소에 대한 누적 합을 계산해나감. (idx 차이 계산시 st에 저장된 가장 마지막과의 차이를 구해야함)
# 굉장히 어렵다...
# ref: https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/723109/Python-solution
# Time complexity : O(MN), Space complexity : O(1)


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        ans = 0
        h = [0] * (M+1)
        for j in range(N):
            st = [(-1, 0)]
            for i in range(M):
                e = mat[i][j]
                h[i] = (e == 1) * (h[i]+1)
                while st and h[st[-1][0]] > h[i]:
                    st.pop()
                # 현재 h[i] 높이의 블록을 포함하는 갯수를 더하면됨. st의 이전 값 다음부터 현재까지.
                # + 이전 블록의 높이에서 연장되서 현재 i까지 오는 블록들. st[-1][1]과 갯수가 동일함.
                ct = (i - st[-1][0]) * h[i] + st[-1][1]
                ans += ct
                st.append((i, ct))
        return ans

    def numSubmat_1(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        ans = 0
        for j in range(N):
            for i in range(M):
                max_i = M
                for n in range(j, N):
                    for m in range(i, max_i):
                        if mat[m][n] == 1:
                            ans += 1
                        else:
                            max_i = min(max_i, m)
                            break
        return ans

