class WordDistance:
    
    def __init__(self, wordsDict: List[str]):
        self.d = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.d[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        """
        sorting 되어있으므로 O(M+N)으로 탐색가능. 
        """
        i, j, ans = 0, 0, float('inf')
        l1, l2 = self.d[word1], self.d[word2]
        while i < len(l1) and j < len(l2):
            ans = min(ans, abs(l1[i]-l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)