# 문제 설명 : cycle 에 속하지 않는 노드를 리턴

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Cycle이 생성된 노드는 False를 리턴해버려서 visited가 1로 설정된 채로 남아있다.
        Cycle이 생성되지 않았으면 visited가 2로 설정되고 True를 리턴.
        """
        visited = defaultdict(int)
        def dfs(node):
            visited[node] = 1
            for dst in graph[node]:
                if visited[dst] == 1 or (visited[dst] == 0 and not dfs(dst)):
                    return False
            visited[node] = 2
            return True
        
        ans = []
        for i in range(len(graph)):
            if visited[i] == 2 or dfs(i):
                ans.append(i)
        return ans
                