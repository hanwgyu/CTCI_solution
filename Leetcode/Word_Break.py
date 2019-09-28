# Solution : DP. 뒷글자부터 시작. 연속으로된 글자를 만들수 있는지 여부를 저장. 
# Trie로 단어를 저장해서 관리.
# Time : O(NM), Space : O(N)

class Node:
    def __init__(self, char : str, end = False):
        self.char = char
        self.end = end
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = Node(None)
    def addString(self, string: str):
        curr_node = self.root
        for c in string:
            if c not in curr_node.children:    
                temp_node = Node(c)
                curr_node.children[c] = temp_node
                curr_node = temp_node
            else:
                curr_node = curr_node.children[c]
        curr_node.end = True
    def findSubstrings(self, string: str):
        ans, curr_node = [], self.root
        for i, c in enumerate(string):
            if c in curr_node.children:
                curr_node = curr_node.children[c]
                if curr_node.end: ans.append(i)
            else:
                return ans
        return ans
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for w in wordDict:
            trie.addString(w)
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        
        for i in reversed(range(len(s))):
            w = s[i:]
            indexs = trie.findSubstrings(w)
            for idx in indexs:
                if i+idx+1 <= len(s) and dp[i+idx+1]:
                    dp[i] = True
                    break
        return dp[0]
        
        
