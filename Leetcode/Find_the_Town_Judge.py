# Solution : inbound 가 N-1이고, outbound 가 0인 노드를 찾음.
# Time : O(|V|+|E|), Space : O(|V|)


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        inbounds, outbounds = [0] * (N + 1), [0] * (N + 1)
        for [i, j] in trust:
            inbounds[j], outbounds[i] = inbounds[j] + 1, outbounds[i] + 1
        for i in range(1, N + 1):
            if outbounds[i] == 0 and inbounds[i] == N - 1:
                return i
        return -1
