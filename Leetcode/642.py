# Trie 구현.
# 현재까지의 substring에 대한 모든 sentences들을 dfs로 돌면서 리턴한 후, sort해서 3개만 출력함.

class Node:
    def __init__(self, c: str):
        self.c = c
        self.child = {} # save tuple of (Node, max_times of all children)
        self.times = 0

class Trie:
    def __init__(self):
        self.root = Node("") # dummy

    def add(self, s: str, times: int):
        node = self.root
        for c in s:
            if c not in node.child:
                node.child[c] = Node(c)
            node = node.child[c]
        node.times += times

    def find_sentences(self, s: str, node: Node) -> List[Tuple[str, int]]:
        """
        s : 현재 노드까지의 str
        """
        if not node:
            return []
        ans = []
        if node.times != 0:
            ans.append((s, node.times))
        for child in node.child.values():
            ans.extend(self.find_sentences(s+child.c, child))
        return ans


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        # Trie 생성
        self.trie = Trie()
        for s, t in zip(sentences, times):
            self.trie.add(s, t)

        # input 함수의 상태를 저장해놓는 변수
        self.s = ""
        self.node = self.trie.root


    def input(self, c: str) -> List[str]:
        if c == "#":
            # add input
            self.trie.add(self.s, 1)
            # Reset
            self.s = ""
            self.node = self.trie.root
            return []
        self.s += c
        if not self.node:
            return []
        self.node = self.node.child[c] if c in self.node.child else None
        result = self.trie.find_sentences(self.s, self.node)
        ans = [s for s, _ in sorted(result, key=lambda x: (-x[1], x[0]))[:3]]
        return ans


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
