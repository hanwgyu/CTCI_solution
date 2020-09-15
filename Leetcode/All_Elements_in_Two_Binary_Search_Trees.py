# Solution : Inorder로 순회, Tree를 한 노드씩 순회할 수 있도록 하여, 노드 값이 작은 tree만 다음 노드로 순회.
# Time : O(N1+N2), Space: O(H1+H2)

# TODO : recursive하게 푸는 방법이 있나?

from collections import deque


class TreeTraversal:
    def __init__(self, root: TreeNode):
        self.node = root
        self.st = []
        self.ready_to_pop = False
        self.next()

    def next(self) -> bool:
        " Inorder traverse to next node "
        while True:
            if self.ready_to_pop:
                self.node = self.st.pop().right
                self.ready_to_pop = False
            elif self.node:
                self.st.append(self.node)
                self.node = self.node.left
            elif self.st:
                self.ready_to_pop = True
                return True
            else:
                return False

    def value(self) -> int:
        " Return current node value "
        return self.st[-1].val if self.st else None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree1, tree2 = TreeTraversal(root1), TreeTraversal(root2)
        ret = []
        v1, v2 = tree1.value(), tree2.value()
        # 두 tree의 현재 노드값을 비교 작은 값을 가진 tree만 traverse
        while v1 is not None and v2 is not None:
            if v1 > v2:
                ret.append(v2)
                tree2.next()
            else:
                ret.append(v1)
                tree1.next()
            v1, v2 = tree1.value(), tree2.value()
        # 방문하지 않은 노드들을 순회
        if tree1.value():
            tree = tree1
        else:
            tree = tree2
        while tree.value() is not None:
            ret.append(tree.value())
            tree.next()
        return ret
