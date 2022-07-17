# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Tree를 DFS로 순회하면서 Graph의 adj list 를 만들고, 
        adj list를 이용해 k 거리에 있는 모든 노드를 리턴
        """
        adj = defaultdict(list)
        
        def dfs(node: TreeNode):
            if not node:
                return
            if node.left:
                adj[node].append(node.left)
                adj[node.left].append(node)     
                dfs(node.left)
            if node.right:
                adj[node].append(node.right)
                adj[node.right].append(node)
                dfs(node.right)
        dfs(root)
        visited, q = set(), deque([(target,k)])
        res = []
        while q:
            node, k_ = q.popleft()
            visited.add(node)
            if k_ == 0:
                res.append(node.val)
            for neighbor in adj[node]:
                if neighbor not in visited and k_ > 0:
                    q.append((neighbor, k_-1))
        return res
                    
                    
                    
                    
