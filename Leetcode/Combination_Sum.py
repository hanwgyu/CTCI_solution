from collections import defaultdict

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def findAllCombinations(target: int):
            if target <= 0 or target in visited:
                return
            for c in candidates:
                t = target-c
                if t > 0:
                    findAllCombinations(t)
                    for e in d[t]:
                        if e[-1] <= c:
                            d[target].append(e+[c])
            visited.add(target)
            
        cs, visited = set(), set()
        d = defaultdict(list)
        
        for c in candidates:
            cs.add(c)
            d[c].append([c])
            
        findAllCombinations(target)
        return d[target]
