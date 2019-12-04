# Solution 1 :
# 1)preorder와 inorder에서 두 숫자 순서가 거꾸로이면 left subtree에 속함.
# 2)preorder와 inorder에서 두 숫자 순서가 그대로이면 right subtree에 속함.
# root부터 preorder순으로 노드를 만들어가면서 추가되지 않은 숫자들만 새롭게 subtree에 배정함.
# Time : O(N^2), Space : O(N^2)

# Solution 2: sol1에서 idx를 넘기도록 개선해 복사비용을 줄임.
# pre_idx를 global하게 관리해, 현재 Tree의 root를 쉽게 찾을 수 있게함.
# Time : O(N), Space : O(N)

class Solution:
    def buildTree_2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def preOrder(in_from: int, in_to: int) -> TreeNode:
            if in_from >= in_to:
                return None
            val = preorder[self.pre_idx]
            self.pre_idx += 1
            in_idx = d_in[val]
            node = TreeNode(val)
            node.left = preOrder(in_from, in_idx)
            node.right = preOrder(in_idx+1, in_to)
            return node
         
        d_in, self.pre_idx = {val:i for i, val in enumerate(inorder)}, 0
        return preOrder(0, len(inorder))
    
    
    def buildTree_1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def preOrder(preorder: List[int]) -> TreeNode:
            if not preorder:
                return None
            val, parent_i = preorder[0], d_in[preorder[0]]
            l, r = [], []
            for i in range(1, len(preorder)):
                e = preorder[i]
                if d_in[e] < parent_i: l.append(e)
                else: r.append(e)
            node = TreeNode(val)
            node.left = preOrder(l)
            node.right = preOrder(r)
            return node
         
        N, d_in = len(preorder), {}
        for j, e in enumerate(inorder):
            d_in[e] = j  
        return preOrder(preorder)
        
        
