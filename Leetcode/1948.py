# 고민 1: 두 폴더가 identical 한지 체크하려면, dfs로 subfolder 리스트를 recursive하게 체크해나아가야함.
# 문제점은 모든 폴더 조합을 체크하려면 너무 계산량이 많아진다는 것.
# 계산량 줄이기 위한 방법 : depth가 같을때만 체크하도록? DP를 사용해 아래쪽 depth에서 True일때만 parent에서 체크하도록?

# 힌트 봄. Trie, hash 사용하라고함.


# 고민 2 : subtree 전체를 string으로 serialize한 후, deleted되지 않은 노드에 대해서 ans를 만들어냄.
# https://leetcode.com/problems/delete-duplicate-folders-in-system/discuss/1361419/Python-Serialize-subtrees-%2B-complexity-analysis-explained 참고

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths):
        root = Node()

        # Trie 생성. Serialize시 동일하게 만들기 위해 sorting 후 진행
        for path in sorted(paths):
            node = root
            for c in path:
                node = node.children[c]

        # Serialize 진행.
        seen = defaultdict(list)

        def dfs_serialize(node: Node) -> str:
            """
            node의 children들에 대한 serialized 된 string을 반환
            child로 갈때마다 '()' 로 묶어서 생성.
            ex) Example 5: (a(x(y)z)b(wx(y)z))
            """
            keys = []
            for c, child in node.children.items():
                keys.append(c + dfs_serialize(child))
            key = ''
            if keys:
                key = "(" + "".join(keys) + ")"
                seen[key].append(node)
            return key

        dfs_serialize(root)

        # 겹치는 부분은 deleted 플래그를 설정.
        for nodes in seen.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        # dfs로 돌면서 제거되지 않은 부분 결과로 출력
        ans = []
        def dfs_make_answer(node: Node, path: List[str]):
            for c, child in node.children.items():
                if not child.deleted:
                    new_path = path + [c]
                    ans.append(new_path)
                    dfs_make_answer(child, new_path)

        dfs_make_answer(root, [])
        return ans
