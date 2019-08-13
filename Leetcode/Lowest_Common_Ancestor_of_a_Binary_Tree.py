# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution : Tree Traversal을 하면서 두 노드 p,q 가 현재 트리에 모두 속하는데, 같은방향에 있지 않으면 해당 트리의 root는 common ancestor.
# Time : O(N), Space : O(H)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def postOrder(node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> (bool, bool): # p,q 포함 여부 리턴
            if not node:
                return (False, False)
            ret_l = postOrder(node.left, p, q)
            ret_r = postOrder(node.right, p ,q)
            if ret_l == (True, True) or ret_r == (True, True):
                return (True, True)
            is_root_p, is_root_q = (node.val == p.val), (node.val == q.val)
            ret = (ret_l[0] | ret_r[0] | is_root_p, ret_l[1] | ret_r[1] | is_root_q)
            if ret[0] == True and ret[1] == True:
                nonlocal ans
                ans = node 
            return ret
        ans = None
        postOrder(root, p, q)
        return ans
        
        
