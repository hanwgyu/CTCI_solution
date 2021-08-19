# 고민 1: 트리로 생성해서,dfs로 돌면서 가장 긴 파일 경로를 리턴.

# 고민 2 : 트리 생성할 필요가 없고, 그냥 순차적으로 max_len를 계산해나아가면됨.

class Node:
    def __init__(self, is_file: bool, l: int):
        self.is_file = is_file
        self.l = l
        self.child = []
        self.parent = None

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        l = defaultdict(int)
        ans = 0
        for line in input.splitlines():
            s = line.lstrip('\t')
            depth = len(line)-len(s)
            if '.' in s:
                ans = max(ans, l[depth-1]+len(s))
            else:
                l[depth] = l[depth-1]+len(s)+1
        return ans

    def lengthLongestPath_1(self, input: str) -> int:
        # make tree
        '''
        /t이 하나 줄어들면 parent로 올라감.
        /t이 하나 늘면 child로 추가함
        '''
        root = Node(False, 0) # dummy node
        cur_node = root
        paths = input.split('\n')
        cur_depth = -1
        for path in paths:
            is_file = True if "." in path else False
            s = path.split('\t')
            print(s)
            depth = len(s) - 1
            l = len(s[-1])
            node = Node(is_file, l)
            # cur_depth를 depth보다 1 작게 유지
            if depth - cur_depth == 2:
                cur_node = cur_node.child[-1]
                cur_depth += 1
            while depth <= cur_depth:
                cur_node = cur_node.parent
                cur_depth -= 1
            node.parent = cur_node
            cur_node.child.append(node)

        self.ans = 0
        def dfs(node: Node, l: int):
            tl = l+node.l
            if node.is_file:
                self.ans = max(self.ans, tl)
            for child in node.child:
                dfs(child, tl+1)
        dfs(root, -1)
        return self.ans
