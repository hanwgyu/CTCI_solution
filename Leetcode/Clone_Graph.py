"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

#Solution : DFS. Time : O(|V|+|E|), Space : O(N)

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node: 'Node') -> 'Node':
            if node in visited:
                return visited[node]
            clone_node = Node(node.val, [])
            visited[node] = clone_node
            for neighbor in node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            return clone_node
        visited = dict()
        return dfs(node)
            
        
