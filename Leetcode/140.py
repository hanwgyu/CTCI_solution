class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, s: str):
        cur = self.root
        for c in s:
            cur = cur.child[c]
        cur.is_word = True
    
    def findSubstrings(self, s: List[str], i: int) -> List[str]:
        ans = []
        cur = self.root
        for j in range(i, len(s)):
            c = s[j]
            if c not in cur.child:
                break
            cur = cur.child[c]
            if cur.is_word:
                ans.append("".join(s[i:j+1]))
        return ans
        

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        dfs
        """
        @lru_cache(maxsize=11)
        def dfs(i):
            if i == len(s):
                return ['']
            ans = []
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    for o in dfs(j):
                        ans.append(s[i:j]+(o and ' '+o))
            return ans
        return dfs(0)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Trie + DP
        뒤부터 시작해서 현재 범위에서 마지막까지의 substring들을 구함.
        DP에는 결과값들을 저장해나아감
        단어 길이가 최대 10이므로 dp를 10까지만 저장함.

        S : len(s), M: len(wordDict), N: max(wordDict, len)
        """

        dp = [[] for _ in range(11)]
        
        # Create Trie
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        """    
        def printTrie(node, word:str=''):
            if not node:
                return
            if node.is_word:
                print(word)
            for c in node.child.keys():
                printTrie(node.child[c], word+c)  
        printTrie(trie.root)
        """
            
        # dp
        s = list(s)
        for i in reversed(range(len(s))):
            dp[i%11] = []
            words = trie.findSubstrings(s, i)
            for word in words:
                # 문자가 가장 끝부분에 존재할때는 그냥 추가함.
                if i+len(word) == len(s):
                    dp[i%11].append(word)
                for l in dp[(i+len(word))%11]:
                    dp[i%11].append(word+" "+l)
        return dp[0]