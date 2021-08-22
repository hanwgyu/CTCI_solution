# 가장 큰 값에서 그 다음 큰 값을 빼면 절대값이 가장 작은 값 d 또는 -d을 얻을 수 있다.
# d를 빼서 (0인 경우를 고려해) d를 제외한 원소들로 구성된 리스트를 새롭게 얻어내고, 위 과정을 반복한다.
# => 이때 제거되지 않는 원소들이 있다..
# 이걸 풀기 위해 pair가 모두 array에 존재할경우 count를 줄여 나가고, 새로운 array로 구해나간다.
# ref : https://leetcode.com/problems/find-array-given-subset-sums/discuss/1418799/Python-Short-solution-(update)-explained


class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        ans = []
        sums = sorted(sums)
        def dfs(sums, n):
            if 0 not in sums: return []
            if n == 1: return [sum(sums)]
            d = sums[-1] - sums[-2]
            ans = []
            for dr in [1, -1]:
                cnt, new = Counter(sums), []
                for num in sums:
                    if cnt[num] == 0 or cnt[num - d*dr] == 0: continue
                    cnt[num] -= 1
                    cnt[num - d*dr] -= 1
                    new.append(num)
                if len(new) == pow(2, n-1):
                    ans.append([-d*dr] + dfs(new, n-1))
            return max(ans, key=len)
        return dfs(sums, n)
