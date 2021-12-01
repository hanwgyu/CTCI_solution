# 첫번째 자리를 decreasing order, 두번째 자리는 increasing order로 sorting해서, 두번째 자리 기준으로 큰 값을 업데이트 해나아감.
# sort후에 값이 같은 경우를 유의해야함. 첫번째 자리와 두번째 자리를 반대로 sorting 했기 때문에 문제 없음.
# Time : O(NlogN), Space : O(1)

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda e:(-e[0], e[1]))
        curr_max = 0
        ans = 0
        for _, p in properties:
            if curr_max <= p:
                curr_max = p
            else:
                ans += 1
        return ans
