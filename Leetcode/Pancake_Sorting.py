# Solution : 뒤에서부터 한칸씩 sort를 늘려나감.
# Time : O(N) , Space : O(N)

# TODO : 최소 횟수로 Sorting하는 방법?


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        # A의 앞에서부터 n개의 원소를 reverse
        def reverse(n: int):
            for i in range(n // 2):
                a, b = i_to_v[n - 1 - i], i_to_v[i]
                i_to_v[i], i_to_v[n - 1 - i] = a, b
                v_to_i[b], v_to_i[a] = v_to_i[a], v_to_i[b]

        # A의 앞에서부터 n개의 원소를 정렬
        def sort(n: int) -> List[int]:
            if n == 1:
                return []
            max_val_i = v_to_i[n]
            ret = []
            if max_val_i + 1 != n:
                if max_val_i + 1 != 1:
                    reverse(max_val_i + 1)
                    ret.append(max_val_i + 1)
                reverse(n)
                ret.append(n)
            return ret + sort(n - 1)

        v_to_i = {a: i for i, a in enumerate(A)}
        i_to_v = {i: a for i, a in enumerate(A)}
        return sort(len(A))
