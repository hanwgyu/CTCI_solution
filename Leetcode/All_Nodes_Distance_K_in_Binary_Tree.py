# Solution : 처음 traverse하면서 target의 height와 root로부터의 위치를 기록해놓음.
# 두번째 traverse시 target의 위와 아래로 나눠 distance에 따른 node들을 출력.
# Time : O(N), Space : O(h)

from typing import Tuple


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def findTarget(
            node: TreeNode, target: int, h: int, path: int
        ) -> Tuple[int, int]:  # return height and path from root
            if not node:
                return None
            if node.val == target:
                return (h, path)
            res_l = findTarget(node.left, target, h + 1, path + (1 << h))
            res_r = findTarget(node.right, target, h + 1, path)
            return res_l if res_l else (res_r if res_r else None)

        def solveDescendants(node: TreeNode, dis: int):
            if not node or dis < 0:
                return
            if dis == 0:
                ans.append(node.val)
            solveDescendants(node.left, dis - 1)
            solveDescendants(node.right, dis - 1)

        def solve(node: TreeNode, path: int, remain_h: int):
            if not node:
                return
            # 1) Add descendants of target
            if remain_h == 0:
                solveDescendants(node, K)
                return
            # 2) Add ancestors of target
            if K - remain_h == 0:
                ans.append(node.val)
            path, go_left = path // 2, path % 2
            # 3) Add other descendants of ancestors of target
            solveDescendants(
                node.right if go_left else node.left, K - remain_h - 1
            )
            solve(node.left if go_left else node.right, path, remain_h - 1)

        ans, res = [], findTarget(root, target.val, 0, 0)
        if not res:
            return None
        solve(root, res[1], res[0])
        return ans
