# Time : O(N+M), Space: O(M) (N: len(sentence), M : len(similarPairs))

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        d = defaultdict(lambda: set())
        for i, (s1, s2) in enumerate(similarPairs):
            d[s1].add(s2)
            d[s2].add(s1)

        for s1, s2 in zip(sentence1, sentence2):
            if s1 != s2 and s2 not in d[s1]:
                return False
        return True
