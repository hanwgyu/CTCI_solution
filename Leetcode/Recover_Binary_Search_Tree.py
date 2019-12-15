# Solution 1 : inorder traverse해서 이상한 두 노드를 찾고 두 노드의 값을 바꿈. 
# val값이 작아질 때가 두번 발생하면 첫번째는 앞쪽노드, 두번째는 뒤쪽노드가 바뀐노드.
# Time : O(N), Space : O(H)

class Solution:
    """
    Do not return anything, modify root in-place instead.
    """
    def recoverTree(self, root: TreeNode) -> None:
        def inorder(node: TreeNode) -> None:
            if not node:
                return
            inorder(node.left) 
            if self.pre_n and self.pre_n.val > node.val:
                self.n2 = node
                if not self.n1: 
                    self.n1 = self.pre_n
                else: 
                    return    
            self.pre_n = node
            inorder(node.right)
        self.n1 = self.n2 = self.pre_n = None
        inorder(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
