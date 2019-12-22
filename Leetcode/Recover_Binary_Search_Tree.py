# Solution 1 : inorder traverse해서 이상한 두 노드를 찾고 두 노드의 값을 바꿈. 
# val값이 작아질 때가 두번 발생하면 첫번째는 앞쪽노드, 두번째는 뒤쪽노드가 바뀐노드.
# Time : O(N), Space : O(H)

# Solution 2 : Morris Inorder Traversal. Space를 사용하지 않는 inorder traversal. 맨 오른쪽 자식 노드를 부모노드에 연결해 stack없이 iterate이후 위로 올라오게 동작시킴.
# node가 오른쪽 자식으로 이동할때 (올라오거나, 오른쪽으로 내려갈때)만 pre_n과의 크기를 비교함.
# Time : O(N), Space : O(1)


class Solution:
    """
    Do not return anything, modify root in-place instead.
    """
    def recoverTree_2(self, root: TreeNode) -> None: 
        n1 = n2 = pre_n = None
        node = root
        while node:
            if node.left:
                temp = node.left
                while temp.right and temp.right != node:
                    temp = temp.right
                if not temp.right:
                    temp.right = node
                    node = node.left
                else:
                    if pre_n and pre_n.val > node.val:
                        n2 = node
                        if not n1: n1 = pre_n
                        #여기는 break문이 있으면 안됨. right가 연결된 상태이기 때문에 right 연결이 끊길때까지 모든 노드를 iterate해야함.
                    pre_n = node
                    temp.right, node = None, node.right    
            else: 
                if pre_n and pre_n.val > node.val:
                    n2 = node
                    if not n1: n1 = pre_n
                pre_n = node
                node = node.right
        n1.val, n2.val = n2.val, n1.val
          
            
    def recoverTree_1(self, root: TreeNode) -> None:
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
