class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """
        dislikes를 edge로 생각하여 그래프를 만들고, dfs로 돌면서 0,1 두 그룹으로 나눔.
        """
        adj_list = defaultdict(list)
        for i, j in dislikes:
            adj_list[i].append(j)
            adj_list[j].append(i)
        
        colors = {}
        
        def dfs(i: int, color: int) -> bool:
            if i in colors:
                return True if colors[i] == color else False
            colors[i] = color
            for j in adj_list[i]:
                if not dfs(j, 1-color):
                    return False
            return True
                
        for i in range(1, n+1):
            if i not in colors and not dfs(i, 0):
                return False
        return True
        