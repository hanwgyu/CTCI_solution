# Union-find

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        d = {}

        def union(s1: str, s2: str):
            d[find(s1)] = find(s2)

        def find(s: str) -> str:
            if s not in d:
                return s
            if d[s] != s:
                return find(d[s])
            return d[s]

        for i, (s1, s2) in enumerate(similarPairs):
            # s가 dict에 없으면 idx를 배정
            for s in [s1, s2]:
                if s not in d:
                    d[s] = s
            # s1, s2를 union.
            union(s1, s2)

        return all(s1 == s2 or find(s1) == find(s2) for s1, s2 in zip(sentence1, sentence2))
