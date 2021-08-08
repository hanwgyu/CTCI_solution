# 고민 1: 모두 계산하는 방법. 특정 노드의 parents로 나아가면서 XOR이 최소인 것들을 찾아감.
# Time limit exceeded

# 고민 2 :
# 모든 노드에 대한 queries를 모두 저장해놓고, dfs로 돌면서 결과를 계산. (노드 search 횟수를 줄일 수 있음)
# dfs로 돌때 현재 노드의 parents들의 2진수 값에 대한 trie를 만들어서 XOR 계산을 O(1)내에 진행함.

from collections import defaultdict

class TrieNode:
    def __init__(self, b: int):
        self.b = b # 0 or 1
        self.children = {} # key : b, val : TrieNode
        self.count = 0

class Trie:
    """
    root가 18자리의 2진수로 표현했을때 가장 앞자리로 시작. child로 가면서 오른쪽으로 한자리씩 표현함
    """
    def __init__(self):
        self.root = TrieNode(-1)

    def increase(self, node: int, count: int):
        # 2 * 10^5 = 110000110101000000
        # insert TrieNodes
        cur = self.root
        for i in reversed(range(18)):
            b = (node >> i) & 1
            if b not in cur.children:
                cur.children[b] = TrieNode(b)
            cur = cur.children[b]
            cur.count += count

    def findMaximumGeneticDiff(self, val: int):
        """
            root에서 시작해서 2진수로 표현했을때 val과 최대한 다른 노드를 선택해 나아감.
        """
        ans = 0
        cur = self.root
        for i in reversed(range(18)):
            b = (val >> i) & 1
            if (1-b) in cur.children and cur.children[1-b].count > 0:
                ans |= (1 << i)
                cur = cur.children[1-b]
            else:
                cur = cur.children[b]
        return ans


class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        node_queries = defaultdict(list) # key : node, val : (val, i)
        for i, (node, val) in enumerate(queries):
            node_queries[node].append((val,i))

        childrens = defaultdict(list) # key : node, val : children of nodes
        for c, p in enumerate(parents):
            childrens[p].append(c)

        trie = Trie()
        ans = [0] * len(queries)
        def dfs(node: int):
            trie.increase(node, 1)
            for val, i in node_queries[node]:
                ans[i] = trie.findMaximumGeneticDiff(val)
            for child in childrens[node]:
                dfs(child)
            trie.increase(node, -1)
        dfs(childrens[-1][0])
        return ans


    def maxGeneticDifference_1(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        for node, val in queries:
            m = 0
            while node != -1:
                m = max(m, node^val)
                node = parents[node]
            ans.append(m)
        return ans
