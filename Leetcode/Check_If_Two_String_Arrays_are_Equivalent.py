# Solution 1
# Time : O(W1+W2), Space : O(W1+W2) (W1, W2: word1, word2 내 모든 str의 총 길이)

# Solution 2
# Time : O(min(W1,W2)), Space : O(1) (W1, W2: word1, word2 내 모든 str의 총 길이)


class Solution:
    def arrayStringsAreEqual_2(self, word1: List[str], word2: List[str]) -> bool:
        return all(c1 == c2 for c1, c2 in itertools.zip_longest(*map(itertools.chain.from_iterable, (word1, word2))))

    def arrayStringsAreEqual_2(self, word1: List[str], word2: List[str]) -> bool:
        def from_iterable(words: List[str]):
            for word in words:
                for c in word:
                    yield c

        def repeat(obj):
            while True:
                yield obj

        def zip_longest(*args):
            iterators = [iter(it) for it in args]
            active = len(iterators)
            while True:
                a = []
                for i, it in enumerate(iterators):
                    try:
                        value = next(it)
                    except StopIteration:
                        active -= 1
                        if not active:
                            return
                        iterators[i] = repeat("-")
                        value = "-"
                    a.append(value)
                yield tuple(a)

        return all(c1 == c2 for c1, c2 in zip_longest(*[from_iterable(word1), from_iterable(word2)]))

    def arrayStringsAreEqual_1(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
