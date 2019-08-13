# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#Time : O(N), Space : O(N)

class Solution:
    def isSymmetric_1(self, root: TreeNode) -> bool:
        def traverse(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return (node1.val == node2.val) and traverse(node1.left, node2.right) and traverse(node1.right, node2.left)   
    
    def isSymmetric_2(self, root: TreeNode) -> bool:
        def preOrder(node: TreeNode, ltor : bool):
            if not node:
                if ltor:
                    a_ltor.append(None)
                else:
                    a_rtol.append(None)
                return
            if ltor:
                a_ltor.append(node.val)
            else:
                a_rtol.append(node.val)
            if ltor:
                preOrder(node.left, ltor)
            preOrder(node.right, ltor)
            if not ltor:
                preOrder(node.left, ltor)
        
        a_ltor, a_rtol = [], []
        preOrder(root, True)
        preOrder(root, False)
        return a_ltor == a_rtol
