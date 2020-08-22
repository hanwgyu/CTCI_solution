# 각 word의 character들을 order에 따른 idx값으로 변환해 전체 words의 순서가 맞는지 확인
# Time : O(N), Space : O(1)


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c: i for i, c in enumerate(order)}
        prev = None
        for word in words:
            a = [d[c] for c in word]
            # list끼리 비교시 첫 원소부터 비교.
            if prev and prev > a:
                return False
            prev = a
        return True
