# 각 숫자에서 갈수있는 다음 항목을 저장해놓고 모든 경우의 수를 계산.
# 특정 값을 지나면 dictionary에 가능 여부를 추가해줘야한다..
# 계산할때 dfs로 도는 방법 말고 없을까?


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        d = {
            0: {1,2,3,4,5,6,7,8,9},
            1: {2,4,5,6,8},
            2: {1,3,4,5,6,7,9},
            3: {2,4,5,6,8},
            4: {1,2,3,5,7,8,9},
            5: {1,2,3,4,6,7,8,9},
            6: {1,2,3,5,7,8,9},
            7: {2,4,5,6,8},
            8: {1,3,4,5,6,7,9},
            9: {2,4,5,6,8}
        }
        d_add = {
            0: [],
            1: [],
            2: [[1,3]], #2를 visit하면 1->3으로 가는 길이 가능해진다.
            3: [],
            4: [[1,7]],
            5: [[1,9],[2,8],[3,7],[4,6]],
            6: [[3,9]],
            7: [],
            8: [[7,9]],
            9: []
        }

        def calc(node: int, n: int, visited: Set[int] = set()) -> int:
            if n == 0:
                return 1
            visited.add(node)
            for src, dst in d_add[node]:
                d[src].add(dst)
                d[dst].add(src)
            ans = sum(calc(i, n-1, visited) for i in (d[node] - visited))
            for src, dst in d_add[node]:
                d[src].remove(dst)
                d[dst].remove(src)
            visited.remove(node)
            return ans
        return sum(calc(0, i) for i in range(m, n+1))
