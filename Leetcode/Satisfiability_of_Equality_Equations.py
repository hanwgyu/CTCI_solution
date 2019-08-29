# Solution : Union-find
# Time : O(N), Space : O(N)

from collections import defaultdict

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(c: str) -> str:
            if colors[c] != c:
                return find(colors[c])
            return c
            
        colors = dict()
        for e in equations:
            if e[0] not in colors:
                colors[e[0]] = e[0]
            if e[3] not in colors:
                colors[e[3]] = e[3]
        
        for e in equations:
            if e[1] == "=":
                colors[find(e[0])] = find(e[3]) 
               
        for e in equations:
            if e[1] == "!" and find(e[0]) == find(e[3]):
                return False
        return True
        
