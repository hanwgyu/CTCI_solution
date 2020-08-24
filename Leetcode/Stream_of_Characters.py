# Solution : Trie 사용. 뒤쪽부터 거꾸로 체크.
# Time : O(MN)(init), O(M)(query) (M : max length of word, N: a number of words)
# Space : O(MN)(init), O(M)(query) (M : max length of word, N: a number of words)

from collections import deque


class Node:
    def __init__(self, char: str, end=False):
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


class StreamChecker:
    def __init__(self, words: List[str]):
        self.d = deque()
        self.trie = Trie()
        for word in words:
            self.trie.addString(word[::-1])

    def query(self, letter: str) -> bool:
        self.d.appendleft(letter)
        curr_node = self.trie.root
        for c in self.d:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]
            if curr_node.end:
                return True
        return curr_node.end


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
