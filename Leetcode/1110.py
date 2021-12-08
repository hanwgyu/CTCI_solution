# 문제 해설 : to_delete로 노드를 제거한 후에, 분리된대로 트리들을 리턴해라.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """
            pre-order traverse
        """
        to_delete = set(to_delete)

        ans = []

        def dfs(node: TreeNode, is_root: bool) -> Optional[TreeNode]:
            if not node:
                return
            is_deleted = node.val in to_delete
            if is_root and not is_deleted:
                ans.append(node)
            node.left = dfs(node.left, is_deleted)
            node.right = dfs(node.right, is_deleted)
            return None if is_deleted else node
        dfs(root, True)
        return ans

    def delNodes_1(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """
            특정 노드를 제거하면 세개로 분리된다. 그 노드의 parent, left child,  right child.
            제거하는 순서가 맨 밑에부터 제거되는게 제일 좋다. post-order traverse
        """
        to_delete = set(to_delete)

        def dfs(parent: TreeNode, node: TreeNode, left: bool) -> List[TreeNode]:
            if not node:
                return []
            ans = dfs(node, node.left, True) + dfs(node, node.right, False)
            if node.val in to_delete:
                if left:
                    parent.left = None
                else:
                    parent.right = None
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
            return ans

        dummy = TreeNode()
        dummy.left = root
        ans = dfs(dummy, root, True)
        # root를 추가
        if root.val not in to_delete:
            ans.append(root)
        return ans
