# 문제 설명 : searchWord를 하나씩 입력할때 prefix가 겹치는 단어 최대 3개를 순서대로 리턴. 

class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, s: str):
        node = self.root
        for c in s:
            node = node.child[c]
        node.end = True
    
    def findAll(self, prefix: str) -> List[str]:
        node = self.root
        for c in prefix:
            node = node.child[c]

        def dfs(prefix, node) -> List[str]:
            res = []
            if node.end == True:
                res.append(prefix)
            for k, v in sorted(node.child.items(), key=lambda e:e[0])[:3]:
                res += dfs(prefix+k, v)
            return res
        return dfs(prefix, node)
    


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
            Trie 구현.
        """
        trie = Trie()
        for p in products:
            trie.add(p)
        res = []
        prefix = ''
        for c in searchWord:
            prefix += c
            l = trie.findAll(prefix)
            res.append(sorted(l)[:3])
        return res
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
            sort 후 binary search.
        """
        products.sort()
        
        prefix = ''
        res = []
        for c in searchWord:
            temp = []
            prefix += c
            i = bisect.bisect_left(products, prefix)
            for j in range(i, i+3):
                if j < len(products) and prefix in products[j]:
                    temp.append(products[j])
            res.append(temp)
        return res