# Solution 1 : Time : O(N), Space: O(H)

# Solution 2 : Morris Tree Traversal. 왼쪽으로 내려갔을때 다시 올라오기위해 Stack이나 Recursion을 사용하지 않도록 구현.(메모리 사이즈 줄일 수 있음)
# 왼쪽 child의 가장 오른쪽 child를 현재 노드의 오른쪽 child와 연결해 traverse가 끝난후에 다시 현재 노드의 오른쪽 child로 이동하도록 구현.
# Time : O(N), Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves_2(self, root: TreeNode) -> int:
        node, ret = root, 0
        while node:
            if node.left:
                temp = node.left
                # Add val to sum
                if not temp.left and not temp.right:
                    ret += temp.val
                # Find right-most node and Connect to right child
                while temp and temp.right:
                    temp = temp.right
                temp.right = node.right
                node = node.left
            else:
                node = node.right
        return ret

    def sumOfLeftLeaves_1(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, is_left: bool):
            if not node:
                return
            if is_left and not node.left and not node.right:
                self.ret += node.val
            dfs(node.left, True)
            dfs(node.right, False)

        self.ret = 0
        dfs(root, False)
        return self.ret
