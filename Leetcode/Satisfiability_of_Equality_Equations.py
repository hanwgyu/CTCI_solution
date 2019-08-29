# Solution : Union-find
# Time : O(N), Space : O(N)

from collections import defaultdict
import string

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(c: str) -> str:
            if colors[c] != c:
                return find(colors[c])
            return c
            
        colors = {c : c for c in string.ascii_lowercase}
        for e in equations:
            if e[1] == "=":
                colors[find(e[0])] = find(e[3])         
        return not any(e[1] == "!" and find(e[0]) == find(e[3]) for e in equations)
