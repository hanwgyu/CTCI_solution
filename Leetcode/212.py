# REMIND: Trie를 쓰는 재미있는 예시

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            # children에 TrieNode 가 없으면, 새로운 TrieNode를 생성함
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

class Solution:
    """
        Trie로 단어를 등록하고, dfs로 돌면서 visited 로 방문한 노드를 재방문 안하고, Trie에 속하는 경우만 방문
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)
            
        def dfs(i: int, j: int, visited: Set[Tuple[int,int]], s:List[str], node: TrieNode) -> List[str]:
            if (i,j) in visited:
                return []
            visited.add((i,j))
            res = []
            if node.is_word:
                # 이미 방문한 노드는 False로 바꿔줘야함 . 이부분이 어려움.
                # ex) ['oa', 'oaa'] 의 경우 False로 안해주면 'oaa'로 못감
                node.is_word = False
                res.append(''.join(s))
            for diff in [(0,1), (0,-1), (1,0), (-1,0)]:
                i_, j_ = i+diff[0], j+diff[1]
                if 0<=i_<M and 0<=j_<N and board[i_][j_] in node.children:
                    res += dfs(i_, j_, visited, s+[board[i_][j_]], node.children[board[i_][j_]])
            visited.remove((i,j))
            return res
            
        res = set()
        M, N = len(board), len(board[0])
        for j in range(N):
            for i in range(M):
                if board[i][j] in trie.root.children:
                    for e in dfs(i, j, set(), [board[i][j]], trie.root.children[board[i][j]]):
                        res.add(e)
        return list(res)