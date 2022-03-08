# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        """
        일종의 Two pointer
        가장 가까운 위치를 먼저 찾고 거기서부터 양쪽으로 k개의 범위 내에서 정답을 찾음.
        가장 가까운 위치를 기준으로 더 큰것과 작은 것을 비교해나아가면서 추가함
        stack에 저장하고, pop을 해나아가면서 추가함.
        
        O(klogN) / O(N)
        """
        def predecessor(smallers):
            """
            smallers[0] 보다 작은 모든 원소들 중 큰 순서대로 추가함.
            """
            node = smallers.pop()
            node = node.left
            while node:
                smallers.append(node)
                node = node.right
            
        def successor(largers):    
            node = largers.pop()
            node = node.right
            while node:
                largers.append(node)
                node = node.left
                    
        res = []
        smallers, largers = [], []  # two stacks tracking smaller and larger nodes
        while root:
            if root.val > target:
                largers.append(root)
                root = root.left
            else:
                smallers.append(root)
                root = root.right
        for _ in range(k):
            if smallers and (not largers or largers and target - smallers[-1].val <= largers[-1].val - target):
                res.append(smallers[-1].val)
                predecessor(smallers)
            else:
                res.append(largers[-1].val)
                successor(largers)
        return res
        
    
    
    def closestKValues1(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        """
        sort된 list를 먼저 만들고,
        k 개의 범위를 정하고 shift
        
        O(N) / O(N)
        """
        def inorder(node) -> List[int]:
            if not node:
                return []
            res = inorder(node.left)
            res.append(node.val)
            res.extend(inorder(node.right))
            return res
        A = inorder(root)
        N, mindiff, minidx = len(A), float('inf'), 0
        for i in range(N-k+1):
            diff = max(abs(target-A[i]), abs(target-A[i+k-1]))
            if mindiff > diff:
                mindiff, minidx= diff, i
        return A[minidx:minidx+k]