# Time : O(9Ck), Space : O(k)


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def isValid(a: int, cur_k: int, cur_n: int) -> bool:
            if (
                a + k - cur_k - 1 > 9
                or (k - cur_k) * (a + a + k - cur_k - 1) / 2 > cur_n
            ):
                return False
            return True

        def dfs(a: int, cur_k: int, cur_n: int, l: List[int]):
            if cur_k >= k:
                return
            l.append(a)
            cur_k, cur_n = cur_k + 1, cur_n - a
            if cur_n == 0:
                ret.append(copy.deepcopy(l))
                l.pop()
                return
            for new_a in range(a + 1, 10):
                if isValid(new_a, cur_k, cur_n):
                    dfs(new_a, cur_k, cur_n, l)
            l.pop()

        ret = []
        for a in range(1, 10):
            if isValid(a, 0, n):
                dfs(a, 0, n, [])
        return ret
